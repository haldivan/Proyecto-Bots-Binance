#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
ANALIZADOR DE ESTADÍSTICAS
Proyecto Bots Binance

Versión : 1.0
Etapa   : 1
Autor   : Xavier Herrera + ChatGPT

Este módulo analiza los archivos generados por los bots.

NO modifica archivos.
NO envía órdenes.
NO se conecta a Binance.
=========================================================
"""

# 0. CONFIGURACION

PESOS_SCORE = {
}

UMBRALES_SCORE = {
}

REGLAS_FORTALEZAS = (
    "F001",
    "F002",
    "F003",
    "F004",
    "F005",
    "F006",
    "F007",
    "F008",
)

REGLAS_ACTIVAS = {
    "F001": True,
    "F002": True,
    "F003": True,
    "F004": False,
    "F005": False,
    "F006": False,
    "F007": False,
    "F008": False,
}

REGLAS_HALLAZGOS = {
    "F001": {
        "nombre": "Ventaja estadística positiva",
        "descripcion": (
            "Determina si la estrategia demuestra "
            "una ventaja estadística sostenible."
        ),
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "profit_factor_min": 1.00,
            "expectancy_min": 0.00,
            "score_min": 55
        }

    },

    "F002": {
        "nombre": "Gestión eficiente del riesgo",
        "descripcion": (
            "Evalúa si la estrategia mantiene una relación "
            "equilibrada entre beneficio, riesgo y "
            "recuperación del capital."
        ),
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "reward_risk_min": 1.50,
            "recovery_factor_min": 1.00,
            "drawdown_max": 15.00
        }
    },

    "F003": {
        "nombre": "Consistencia operativa",
        "descripcion": "...",
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "expectancy_min": 0.0,
            "recovery_factor_min": 1.50,
            "max_ratio_racha_perdedora": 0.10
        }
    }
}


from pathlib import Path
from datetime import datetime

# import numpy as np
import pandas as pd

# 1. INICIALIZACION
class AnalizadorEstadisticas:
    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent
        self.datos_dir = self.base_dir / "datos"
        self.reportes_dir = self.base_dir / "reportes"
        self.reportes_dir.mkdir(parents=True, exist_ok=True)
        self.bot = ""
        self.nombre_bot = ""
        self.archivo = None
        self.df = None
        self.df_cerradas = None
        self.df_abiertas = None
        self.fecha_analisis = datetime.now()
    
    # --------------------------------------------------

    # 2. CARGA Y PREPARACIÓN DE DATOS
    def obtener_configuracion_regla(self, codigo):
        """
        Devuelve la configuración oficial de una regla
        del Motor de Hallazgos.
        """
        return REGLAS_HALLAZGOS[codigo]

    def seleccionar_bot(self):
        print("\n" + "=" * 55)
        print("        ANALIZADOR DE ESTADÍSTICAS")
        print("=" * 55)
        print("1) Bot Crypto")
        print("2) Bot TradFi")
        print("=" * 55)

        while True:
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                self.bot = "CRYPTO"
                self.nombre_bot = "Bot Crypto"
                self.archivo = self.datos_dir / "estadisticas_crypto.csv"
                break

            elif opcion == "2":
                self.bot = "TRADFI"
                self.nombre_bot = "Bot TradFi"
                self.archivo = self.datos_dir / "estadisticas_tradfi.csv"
                break

            print("Opción inválida.")

    # --------------------------------------------------

    def cargar_datos(self):
        if not self.archivo.exists():
            raise FileNotFoundError(f"No existe:\n{self.archivo}")
        self.df = pd.read_csv(self.archivo, encoding="utf-8")

        # Verificar que el archivo no esté vacío
        if self.df.empty:
            raise ValueError("El archivo no contiene registros.")

        # Validar columnas obligatorias
        self.validar_columnas()
    # --------------------------------------------------

    def validar_columnas(self):
        if self.bot == "CRYPTO":
            columnas_obligatorias = ["fecha_hora", "simbolo", "direccion", "precio_entrada", "tp", "sl", "score", "version", "fecha_hora_fin",
                                     "PnL", "ROI"]
        else:
            columnas_obligatorias = ["fecha_hora", "simbolo", "direccion", "precio_entrada", "tp", "sl", "estado"]

        columnas_faltantes = [
            c for c in columnas_obligatorias
            if c not in self.df.columns
        ]
        if columnas_faltantes:
            raise ValueError(f"Faltan columnas obligatorias: {columnas_faltantes}")


    def limpiar_datos(self):
        if self.df is None:
            raise ValueError("No existen datos cargados.")

        columnas_fecha = ["fecha_hora", "fecha_hora_fin", "fecha_fin"]

        for col in columnas_fecha:
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col], errors="coerce")

        if "PnL" in self.df.columns:
            self.df["PnL"] = pd.to_numeric(self.df["PnL"], errors="coerce")

        if "score" in self.df.columns:
            self.df["score"] = pd.to_numeric(self.df["score"], errors="coerce")

        if "ROI" in self.df.columns:
            self.df["ROI"] = (self.df["ROI"].astype(str).str.replace("%", "", regex=False).str.strip())
            self.df["ROI"] = pd.to_numeric(self.df["ROI"], errors="coerce")

        if self.bot == "CRYPTO":
            self.df_cerradas = self.df[self.df["fecha_hora_fin"].notna()].copy()
            self.df_abiertas = self.df[self.df["fecha_hora_fin"].isna()].copy()

        else:
            self.df_cerradas = self.df[self.df["estado"] != "ABIERTA"].copy()
            self.df_abiertas = self.df[self.df["estado"] == "ABIERTA"].copy()

            # -----------------------------------------
            # Normalización para análisis estadístico
            # -----------------------------------------
            
            self.df_cerradas["precio_entrada"] = pd.to_numeric(self.df_cerradas["precio_entrada"], errors="coerce")
            self.df_cerradas["precio_cierre"] = pd.to_numeric(self.df_cerradas["precio_cierre"], errors="coerce")

            self.df_cerradas["PnL"] = (self.df_cerradas["precio_cierre"] - self.df_cerradas["precio_entrada"])

            # Si es SHORT se invierte el signo

            mask_short = self.df_cerradas["direccion"].str.contains("SHORT", case=False, na=False)
            self.df_cerradas.loc[mask_short, "PnL"] *= -1
            self.df_cerradas["ROI"] = (
                self.df_cerradas["PnL"] /
                self.df_cerradas["precio_entrada"]
            ) * 100

            self.df_cerradas["direccion"] = (
                self.df_cerradas["direccion"]
                .str.upper()
                .str.replace("ORDEN_COMPRA_", "", regex=False)
                .str.replace("ORDEN_VENTA_", "", regex=False)
            )

    # --------------------------------------------------
    # 3. MOTOR ESTADÍSTICO
    # 3.1 Validación
    def validar_consistencia(self):
        """
        Verifica la consistencia de los datos antes de realizar
        cualquier análisis estadístico.

        No modifica el DataFrame.
        Únicamente informa advertencias.
        """
        fechas_invalidas = 0

        print("\n" + "=" * 55)
        print("VALIDACIÓN DE CONSISTENCIA")
        print("=" * 55)

        advertencias = 0

        # -----------------------------------------
        # Registros duplicados
        # -----------------------------------------

        duplicados = self.df.duplicated().sum()

        if duplicados == 0:
            print("✓ Sin registros duplicados")
        else:
            print(f"⚠ {duplicados} registros duplicados")
            advertencias += 1

        # -----------------------------------------
        # PnL nulo
        # -----------------------------------------

        pnl_nulos = self.df_cerradas["PnL"].isna().sum()

        if pnl_nulos == 0:
            print("✓ Sin PnL nulos")
        else:
            print(f"⚠ {pnl_nulos} operaciones con PnL nulo")
            advertencias += 1

        # -----------------------------------------
        # ROI nulo
        # -----------------------------------------

        roi_nulos = self.df_cerradas["ROI"].isna().sum()

        if roi_nulos == 0:
            print("✓ Sin ROI nulos")
        else:
            print(f"⚠ {roi_nulos} operaciones con ROI nulo")
            advertencias += 1

        # -----------------------------------------
        # Fechas
        # -----------------------------------------

        if self.bot == "CRYPTO":
            if "fecha_hora_fin" in self.df_cerradas.columns:
                fechas_invalidas = (self.df_cerradas["fecha_hora_fin"] < self.df_cerradas["fecha_hora"]).sum()
        else:
            if "fecha_fin" in self.df_cerradas.columns:
                fechas_invalidas = (self.df_cerradas["fecha_fin"] < self.df_cerradas["fecha_hora"]).sum()

        if fechas_invalidas == 0:
            print("✓ Fechas consistentes")
        else:
            print(f"⚠ {fechas_invalidas} operaciones con fechas inválidas")
            advertencias += 1

        # -----------------------------------------
        # Dirección
        # -----------------------------------------

        direcciones_invalidas = (~self.df_cerradas["direccion"].isin(["LONG", "SHORT"])).sum()

        if direcciones_invalidas == 0:
            print("✓ Direcciones válidas")
        else:
            print(f"⚠ {direcciones_invalidas} direcciones desconocidas")
            advertencias += 1

        # -----------------------------------------
        # Resumen
        # -----------------------------------------

        print("-" * 55)

        if advertencias == 0:
            print("Dataset válido para análisis.")
        else:
            print(f"Se detectaron {advertencias} advertencias.")
        

        # --------------------------------------------------


    # 3.2 Métricas Básicas
    def calcular_metricas(self, df):
        """
        Calcula las métricas básicas para cualquier subconjunto
        de operaciones cerradas.
        """
        total = len(df)

        if total == 0:
            return {"total": 0, "ganadoras": 0, "perdedoras": 0, "neutras": 0, "win_rate": 0.0, "pnl": 0.0, "roi": 0.0}

        ganadoras = (df["PnL"] > 0).sum()
        perdedoras = (df["PnL"] < 0).sum()
        neutras = (df["PnL"] == 0).sum()

        operaciones_validas = ganadoras + perdedoras
        win_rate = (
            ganadoras / operaciones_validas * 100
            if operaciones_validas > 0
            else 0
        )

        pnl = df["PnL"].sum()
        roi = (df["ROI"].dropna().mean())
        if pd.isna(roi): roi = 0

        return {"total": total, "ganadoras": ganadoras, "perdedoras": perdedoras, "neutras": neutras, "win_rate": win_rate, "pnl": pnl, "roi": roi}

    # --------------------------------------------------

    def obtener_metricas_financieras(self, df):
        """
        Calcula las principales métricas financieras de un conjunto
        de operaciones cerradas.

        Este método será la base para:
            - Profit Factor
            - Expectancy
            - Reportes financieros
        """

        total = len(df)

        if total == 0:
            return {"operaciones": 0, "ganancia_bruta": 0.0, "perdida_bruta": 0.0, "profit_factor": 0.0, "expectancy": 0.0, 
                    "promedio_ganancia": 0.0, "promedio_perdida": 0.0, "reward_risk": 0.0, "recovery_factor": 0.0, "mejor_operacion": 0.0, 
                    "peor_operacion": 0.0, 
                    "pnl_total": 0.0, 
                    "roi_promedio": 0.0}

        # -----------------------------------------
        # Operaciones ganadoras y perdedoras
        # -----------------------------------------

        ganadoras = df[df["PnL"] > 0]
        perdedoras = df[df["PnL"] < 0]

        # -----------------------------------------
        # Ganancia y pérdida bruta
        # -----------------------------------------

        ganancia_bruta = ganadoras["PnL"].sum()
        perdida_bruta = abs(perdedoras["PnL"].sum())

        # -----------------------------------------
        # Profit Factor
        # -----------------------------------------

        if perdida_bruta > 0:
            profit_factor = ganancia_bruta / perdida_bruta
        else:
            profit_factor = float("inf")

        # -----------------------------------------
        # Promedios
        # -----------------------------------------

        promedio_ganancia = (
            ganadoras["PnL"].mean()
            if len(ganadoras) > 0
            else 0
        )

        promedio_perdida = (
            abs(perdedoras["PnL"].mean())
            if len(perdedoras) > 0
            else 0
        )

        # -----------------------------------------
        # Relación Riesgo / Beneficio
        # -----------------------------------------

        if promedio_perdida > 0:
            reward_risk = promedio_ganancia / promedio_perdida
        else:
            reward_risk = float("inf")

        # -----------------------------------------
        # Win Rate
        # -----------------------------------------

        operaciones_validas = len(ganadoras) + len(perdedoras)
        win_rate = (
            len(ganadoras) / operaciones_validas
            if operaciones_validas > 0
            else 0
        )

        # -----------------------------------------
        # Expectancy
        # -----------------------------------------

        expectancy = (
            (win_rate * promedio_ganancia)
            -
            ((1 - win_rate) * promedio_perdida)
        )

        # -----------------------------------------
        # Maximum Drawdown
        # -----------------------------------------

        mdd = self.obtener_max_drawdown()["max_drawdown"]

        # -----------------------------------------
        # Recovery Factor
        # -----------------------------------------

        if abs(mdd) > 0:
            recovery_factor = df["PnL"].sum() / abs(mdd)
        else:
            recovery_factor = 0

        # -----------------------------------------
        # ROI promedio
        # -----------------------------------------

        roi_promedio = df["ROI"].dropna().mean()
        if pd.isna(roi_promedio):
            roi_promedio = 0

        # -----------------------------------------
        # Sharpe Ratio (simplificado)
        # -----------------------------------------

        # roi_std = df["ROI"].dropna().std()
        # if pd.isna(roi_std) or roi_std == 0:
        #     sharpe = 0
        # else:
        #     sharpe = roi_promedio / roi_std

        # -----------------------------------------
        # Resultado
        # -----------------------------------------

        return {"operaciones": total, 
                "ganancia_bruta": ganancia_bruta, 
                "perdida_bruta": perdida_bruta, 
                "profit_factor": profit_factor,
                 "expectancy": expectancy, 
                 "promedio_ganancia": promedio_ganancia, 
                 "promedio_perdida": promedio_perdida, 
                 "reward_risk": reward_risk,
                 "recovery_factor": recovery_factor,
                 "mejor_operacion": df["PnL"].max(), 
                 "peor_operacion": df["PnL"].min(), 
                 "pnl_total": df["PnL"].sum(), 
                 "roi_promedio": roi_promedio
                 }

    # --------------------------------------------------

    def obtener_curva_capital(self):
        """
        Construye la curva de capital acumulada
        a partir del PnL de las operaciones cerradas.
        """

        df = self.df_cerradas.copy()

        if len(df) == 0:
            return df

        # Orden cronológico
        df = df.sort_values("fecha_hora")

        # Capital acumulado
        df["capital"] = df["PnL"].cumsum()

        return df

    # --------------------------------------------------

    def obtener_max_drawdown(self):
        """
        Calcula el Maximum Drawdown (MDD) a partir de la
        curva de capital acumulada.
        """

        df = self.obtener_curva_capital()

        # if df.empty:
        #    return {"max_drawdown": 0.0, "max_drawdown_pct": 0.0, "capital_maximo": 0.0, "capital_minimo": 0.0}

        if df.empty:
            return {"max_drawdown": 0.0, "capital_maximo": 0.0, "capital_minimo": 0.0}

        # Máximo histórico alcanzado hasta cada operación
        df["capital_max"] = df["capital"].cummax()

        # Drawdown absoluto
        df["drawdown"] = df["capital"] - df["capital_max"]

        # Drawdown porcentual
        # df["drawdown_pct"] = 0.0

        mask = df["capital_max"] != 0

        # df.loc[mask, "drawdown_pct"] = (df.loc[mask, "drawdown"] / df.loc[mask, "capital_max"]) * 100

        # return {"max_drawdown": df["drawdown"].min(), "max_drawdown_pct": df["drawdown_pct"].min(), "capital_maximo": df["capital"].max(),
        #        "capital_minimo": df["capital"].min()}

        return {"max_drawdown": df["drawdown"].min(), "capital_maximo": df["capital"].max(),
                "capital_minimo": df["capital"].min()}

    # --------------------------------------------------

    def obtener_rachas(self):
        """
        Calcula las rachas máximas de operaciones
        ganadoras y perdedoras consecutivas.
        """

        df = self.df_cerradas.sort_values("fecha_hora").copy()
        
        if df.empty:
            return {"max_ganadoras": 0, "max_perdedoras": 0, "racha_actual": "", "longitud_actual": 0}

        resultados = []

        for pnl in df["PnL"]:
            if pnl > 0:
                resultados.append("G")
            elif pnl < 0:
                resultados.append("P")
            else:
                resultados.append("N")

        max_ganadoras = 0
        max_perdedoras = 0

        actual_g = 0
        actual_p = 0

        for r in resultados:

            if r == "G":
                actual_g += 1
                actual_p = 0

            elif r == "P":
                actual_p += 1
                actual_g = 0

            else:
                actual_g = 0
                actual_p = 0

            max_ganadoras = max(max_ganadoras, actual_g)
            max_perdedoras = max(max_perdedoras, actual_p)

        # ------------------------------------------
        # Racha actual
        # ------------------------------------------

        ultima = resultados[-1]
        longitud = 0
        for r in reversed(resultados):
            if r == ultima:
                longitud += 1
            else:
                break

        nombre = {"G": "Ganadoras", "P": "Perdedoras", "N": "Neutras"}

        return {
            "max_ganadoras": max_ganadoras,
            "max_perdedoras": max_perdedoras,
            "racha_actual": nombre[ultima],
            "tipo_actual": ultima,
            "longitud_actual": longitud
        }
    
    # --------------------------------------------------

    def obtener_resumen(self):
        return {"Bot": self.nombre_bot, "Archivo": self.archivo.name, "Fecha análisis": self.fecha_analisis.strftime("%Y-%m-%d %H:%M:%S"),
                "Registros": len(self.df), "Operaciones cerradas": len(self.df_cerradas), "Operaciones abiertas": len(self.df_abiertas),
                 "Columnas": len(self.df.columns)}

    # --------------------------------------------------

    def obtener_long_short(self):
        direcciones = {}
        for direccion in ["LONG", "SHORT"]:
            df_dir = self.df_cerradas[self.df_cerradas["direccion"] == direccion]
            direcciones[direccion] = self.calcular_metricas(df_dir)
        return direcciones
    
    # --------------------------------------------------

    def obtener_estadisticas_simbolos(self):
        """
        Calcula las estadísticas de cada símbolo.
        """

        estadisticas = {}
        simbolos = sorted(self.df_cerradas["simbolo"].unique())
        for simbolo in simbolos:
            df_simbolo = self.df_cerradas[self.df_cerradas["simbolo"] == simbolo]
            estadisticas[simbolo] = self.calcular_metricas(df_simbolo)
        return estadisticas

    # --------------------------------------------------

    # 3.3 Diagnóstico Automático
    def obtener_metricas_diagnostico(self):
        """
        Reúne todas las métricas necesarias para el
        Diagnóstico Automático.

        No interpreta resultados.
        No imprime información.
        Únicamente centraliza las métricas calculadas
        por otros métodos.
        """

        financieras = self.obtener_metricas_financieras(self.df_cerradas)
        drawdown = self.obtener_max_drawdown()
        rachas = self.obtener_rachas()

        metricas = {}

        # ----------------------------
        # Rendimiento
        # ----------------------------

        metricas["operaciones"] = financieras["operaciones"]
        metricas["profit_factor"] = financieras["profit_factor"]
        metricas["reward_risk"] = financieras["reward_risk"]
        metricas["expectancy"] = financieras["expectancy"]
        metricas["recovery_factor"] = financieras["recovery_factor"]

        metricas["roi_promedio"] = financieras["roi_promedio"]
        metricas["pnl_total"] = financieras["pnl_total"]

        # ----------------------------
        # Riesgo
        # ----------------------------

        metricas["max_drawdown"] = drawdown["max_drawdown"]

        # ----------------------------
        # Operación
        # ----------------------------

        resumen = self.calcular_metricas(self.df_cerradas)

        metricas["win_rate"] = resumen["win_rate"]

        # ----------------------------
        # Rachas
        # ----------------------------

        metricas["racha_ganadora"] = rachas["max_ganadoras"]
        metricas["racha_perdedora"] = rachas["max_perdedoras"]

        metricas["racha_actual"] = rachas["racha_actual"]
        metricas["tipo_actual"] = rachas["tipo_actual"]
        metricas["longitud_actual"] = rachas["longitud_actual"]

        metricas["ratio_racha_perdedora"] = (
            rachas["max_perdedoras"] / financieras["operaciones"]
            if financieras["operaciones"] > 0
            else 0
        )

        return metricas
        
    # --------------------------------------------------

    def obtener_score_estrategico(self, m):
        """
        Calcula un Score Estratégico (0-100)
        basado en las principales métricas del sistema.
        """

        # m = self.obtener_metricas_diagnostico()

        score = 0

        # -----------------------------------------
        # Profit Factor (30 puntos)
        # -----------------------------------------

        if m["profit_factor"] >= 2:
            score += 30
        elif m["profit_factor"] >= 1.5:
            score += 25
        elif m["profit_factor"] >= 1.2:
            score += 20
        elif m["profit_factor"] >= 1:
            score += 15
        elif m["profit_factor"] >= 0.8:
            score += 8

        # -----------------------------------------
        # Expectancy (20 puntos)
        # -----------------------------------------

        if m["expectancy"] > 0:
            score += 20

        # -----------------------------------------
        # Reward / Risk (20 puntos)
        # -----------------------------------------

        if m["reward_risk"] >= 2:
            score += 20
        elif m["reward_risk"] >= 1.5:
            score += 16
        elif m["reward_risk"] >= 1:
            score += 10

        # -----------------------------------------
        # Win Rate (15 puntos)
        # -----------------------------------------

        if m["win_rate"] >= 60:
            score += 15
        elif m["win_rate"] >= 50:
            score += 12
        elif m["win_rate"] >= 40:
            score += 8
        elif m["win_rate"] >= 30:
            score += 4

        # -----------------------------------------
        # Recovery Factor (10 puntos)
        # -----------------------------------------

        if m["recovery_factor"] >= 2:
            score += 10
        elif m["recovery_factor"] >= 1:
            score += 6

        # -----------------------------------------
        # Racha perdedora (5 puntos)
        # -----------------------------------------

        if m["racha_perdedora"] <= 5:
            score += 5
        elif m["racha_perdedora"] <= 10:
            score += 3

        # -----------------------------------------
        # Clasificación
        # -----------------------------------------

        if score >= 85:
            nivel = "EXCELENTE"

        elif score >= 70:
            nivel = "BUENO"

        elif score >= 55:
            nivel = "ACEPTABLE"

        elif score >= 40:
            nivel = "DÉBIL"

        else:
            nivel = "CRÍTICO"

        return {
            "score": score,
            "nivel": nivel
        }
    # --------------------------------------------------

    def obtener_diagnostico(self):
        """
        Interpreta de forma integrada las métricas
        calculadas por el analizador.

        El objetivo no es evaluar indicadores aislados,
        sino identificar las posibles causas del
        desempeño de la estrategia.
        """

        m = self.obtener_metricas_diagnostico()

        score = self.obtener_score_estrategico(m)

        fortalezas = []
        debilidades = []
        observaciones = []
        conclusiones = []

        # ======================================================
        # Evaluación individual
        # ======================================================

        if m["profit_factor"] >= 1.30:
            fortalezas.append("Profit Factor sólido.")

        elif m["profit_factor"] >= 1:
            observaciones.append("Profit Factor aceptable.")

        else:
            debilidades.append("Profit Factor inferior a 1.")

        # ---------------------------------------------

        if m["expectancy"] > 0:
            fortalezas.append("Expectancy positiva.")
        else:
            debilidades.append("Expectancy negativa.")

        # ---------------------------------------------

        if m["reward_risk"] >= 1.50:
            fortalezas.append("Relación Reward/Risk favorable.")
        else:
            observaciones.append("Reward/Risk mejorable.")

        # ---------------------------------------------

        if m["recovery_factor"] > 1:
            fortalezas.append("Recovery Factor adecuado.")
        else:
            debilidades.append("Recovery Factor bajo.")

        # ---------------------------------------------

        if m["win_rate"] >= 50:
            fortalezas.append("Win Rate competitivo.")

        elif m["win_rate"] >= 40:
            observaciones.append("Win Rate moderado.")

        else:
            debilidades.append("Win Rate reducido.")

        # ======================================================
        # Interpretación integrada
        # ======================================================

        # Caso 1
        if (m["reward_risk"] >= 1.5 and m["profit_factor"] < 1 and m["win_rate"] < 40):

            conclusiones.append(
                "Las operaciones ganadoras generan un beneficio "
                "adecuado, pero la frecuencia de aciertos es "
                "insuficiente para sostener la rentabilidad."
            )

        # ------------------------------------------------------

        if (m["reward_risk"] < 1 and m["win_rate"] >= 50):

            conclusiones.append(
                "La estrategia presenta una buena tasa de aciertos, "
                "pero las pérdidas son demasiado grandes respecto "
                "a las ganancias."
            )

        # ------------------------------------------------------

        if (m["recovery_factor"] < 0 and m["max_drawdown"] < 0):

            conclusiones.append(
                "La estrategia aún no logra recuperar las pérdidas "
                "acumuladas reflejadas en la curva de capital."
            )

        # ------------------------------------------------------

        if m["racha_perdedora"] >= 10:

            conclusiones.append(
                f"Se identificó una racha máxima de "
                f"{m['racha_perdedora']} pérdidas consecutivas, "
                "lo que evidencia un periodo prolongado de bajo "
                "desempeño."
            )

        # ======================================================
        # Recomendación metodológica
        # ======================================================

        if m["operaciones"] < 50:

            recomendacion = (
                "La muestra estadística aún es insuficiente para "
                "considerar modificaciones en la estrategia."
            )

        elif m["operaciones"] < 70:

            recomendacion = (
                "La estrategia dispone de una muestra mínima para "
                "iniciar su evaluación, pero se recomienda continuar "
                "recopilando operaciones antes de optimizarla."
            )

        else:
            if m["profit_factor"] >= 1:

                recomendacion = (
                    "La muestra disponible permite iniciar el análisis "
                    "de optimización de la estrategia."
                )

            else:

                recomendacion = (
                    "Aunque la muestra ya es representativa, las métricas "
                    "actuales sugieren revisar la estrategia antes de "
                    "plantear nuevas optimizaciones."
                )

        return {
        #    "estado": estado,
            "fortalezas": fortalezas,
            "debilidades": debilidades,
            "observaciones": observaciones,
            "conclusiones": conclusiones,
            "recomendacion": recomendacion,

            "score": score["score"],
            "nivel": score["nivel"],
        }
    # --------------------------------------------------

    # ============================================================
    # 4. MOTORES DE INTERPRETACIÓN
    # ============================================================

    # ------------------------------------------------------------
    # 4.1 MOTOR DE EVIDENCIA
    # ------------------------------------------------------------
    #
    # Responsabilidad:
    #   Consolidar hechos objetivos a partir de las métricas y del
    #   diagnóstico para determinar el nivel de evidencia de la
    #   estrategia.
    #
    # Este módulo:
    #   ✓ Consume información existente.
    #   ✓ No recalcula indicadores.
    #   ✓ No modifica estadísticas.
    # ------------------------------------------------------------

    def obtener_evidencia(self):
        """
        Genera evidencia objetiva sobre el comportamiento
        estadístico de la estrategia.

        No interpreta resultados.
        Únicamente resume hechos cuantificables.
        """

        evidencia = {}

        df = self.df_cerradas.copy()

        if df.empty:
            return evidencia

        # ==================================================
        # RESULTADO POR SÍMBOLO
        # ==================================================

        pnl_simbolos = (df.groupby("simbolo")["PnL"].sum().sort_values(ascending=False))

        evidencia["mejor_simbolo"] = pnl_simbolos.idxmax()
        evidencia["mejor_pnl"] = pnl_simbolos.max()

        evidencia["peor_simbolo"] = pnl_simbolos.idxmin()
        evidencia["peor_pnl"] = pnl_simbolos.min()

        # ==================================================
        # GANANCIAS
        # ==================================================
        ganancias = (df[df["PnL"] > 0].groupby("simbolo")["PnL"].sum().sort_values(ascending=False))

        evidencia["ganancias"] = ganancias

        if not ganancias.empty:
            evidencia["simbolo_mayor_ganancia"] = ganancias.idxmax()
            evidencia["aporte_ganancias"] = (ganancias.max() / ganancias.sum()) * 100

        else:
            evidencia["simbolo_mayor_ganancia"] = "-"
            evidencia["aporte_ganancias"] = 0

        # ==================================================
        # PÉRDIDAS
        # ==================================================

        perdidas = (df[df["PnL"] < 0].groupby("simbolo")["PnL"].sum().abs().sort_values(ascending=False))

        evidencia["perdidas"] = perdidas

        if not perdidas.empty:
            evidencia["simbolo_mayor_perdida"] = perdidas.idxmax()
            evidencia["aporte_perdidas"] = (perdidas.max() / perdidas.sum()) * 100

        else:
            evidencia["simbolo_mayor_perdida"] = "-"
            evidencia["aporte_perdidas"] = 0

        # ==================================================
        # LONG vs SHORT
        # ==================================================

        pnl_direccion = (df.groupby("direccion")["PnL"].sum().sort_values(ascending=False))

        evidencia["pnl_direccion"] = pnl_direccion

        if not pnl_direccion.empty:
            evidencia["mejor_direccion"] = pnl_direccion.idxmax()
            evidencia["mejor_direccion_pnl"] = pnl_direccion.max()

        else:
            evidencia["mejor_direccion"] = "-"
            evidencia["mejor_direccion_pnl"] = 0

        # ==================================================
        # CONCENTRACIÓN DE PÉRDIDAS
        # ==================================================

        if len(perdidas) >= 2:
            evidencia["drawdown_top2"] = (perdidas.iloc[:2].sum() / perdidas.sum()) * 100

        else:
            evidencia["drawdown_top2"] = 0

        # ==================================================
        # TAMAÑO DE MUESTRA
        # ==================================================

        evidencia["operaciones"] = len(df)

        evidencia["muestra_suficiente"] = (len(df) >= 100)

        # ==================================================
        # VERSIONES
        # ==================================================

        if "version" in df.columns:
            evidencia["versiones"] = sorted(df["version"].dropna().unique().tolist())
        else:
            evidencia["versiones"] = []

        # ==================================================
        # SCORE
        # ==================================================

        if "score_modelo" in df.columns:
            evidencia["score_modelos"] = sorted(df["score_modelo"].dropna().unique().tolist())
        else:
            evidencia["score_modelos"] = []
        return evidencia

        # --------------------------------------------------

    # ------------------------------------------------------------
    # 4.2 MOTOR DE HALLAZGOS ESTRATÉGICOS
    # ------------------------------------------------------------
    #
    # Estado:
    #   Implementación inicial completada.
    # Versión: 1.0
    # Responsabilidad:
    #   Transformar el Diagnóstico Automático y el Motor de Evidencia
    #   en conocimiento accionable para apoyar la evolución de la
    #   estrategia.
    #
    # Este módulo NO recalcula indicadores.
    #
    # Entradas:
    #   - métricas
    #   - diagnóstico
    #   - evidencia
    #
    # Salidas:
    #   - fortalezas estratégicas
    #   - debilidades estratégicas
    #   - oportunidades
    #   - riesgos
    #   - prioridades
    #   - conclusión general
    # ------------------------------------------------------------    


    def obtener_hallazgos(self, metricas, diagnostico, evidencia):
        """
        Motor de Hallazgos Estratégicos.

        Responsabilidad:
            Transformar la información generada por el Motor
            Estadístico, el Diagnóstico Automático y el Motor
            de Evidencia en conocimiento accionable.

        Este módulo:
            ✓ No recalcula métricas.
            ✓ No modifica datos.
            ✓ Consume únicamente información existente.
        """

        hallazgos = {
            "fortalezas": self.obtener_fortalezas_estrategicas(
                metricas,
                diagnostico,
                evidencia
            ),
            "debilidades": [],
            "riesgos": [],
            "oportunidades": [],
            "prioridades": [],
            "conclusion_general": []
        }

        return hallazgos

    def obtener_fortalezas_estrategicas(self, metricas, diagnostico, evidencia):
        """
        Ejecuta todas las reglas registradas
        para Fortalezas Estratégicas.
        """
        fortalezas = []

        for codigo in REGLAS_FORTALEZAS:
            regla = getattr(self, f"aplicar_regla_{codigo}", None)

            if regla is None:
                continue

            resultado = regla(metricas, diagnostico, evidencia)

            if resultado and resultado not in fortalezas:
                fortalezas.append(resultado)

        return fortalezas

        # reglas = (
        #     self.aplicar_regla_F001,
        #     self.aplicar_regla_F002,
        #     self.aplicar_regla_F003,
        #     self.aplicar_regla_F004,
        #     self.aplicar_regla_F005
        # )

        # for regla in reglas:
        #     resultado = regla(metricas, diagnostico, evidencia)
        #     if resultado and resultado not in fortalezas:
        #         fortalezas.append(resultado)

        # return fortalezas
    
    def aplicar_regla_F001(self, metricas, diagnostico, evidencia):
        """
        ==========================================================
        REGLA F-001

        Nombre:
            Ventaja estadística positiva.

        Prioridad:
            Alta

        Evidencia utilizada:
            • Profit Factor
            • Expectancy

        Condición:
            Profit Factor >= 1
            Expectancy > 0

        Interpretación:
            La estrategia presenta evidencia de una ventaja
            estadística positiva.
        Decisión que permite tomar:
            Continuar evaluando la estrategia sin modificar
            su estructura principal.
        ==========================================================
        """

    #    if (metricas["profit_factor"] >= 1 and metricas["expectancy"] > 0 and diagnostico["score"] >= 55):
    #    cfg = self.obtener_configuracion_regla("F001")["parametros"]
        cfg = self.obtener_configuracion_regla("F001")
        p = cfg["parametros"]

        if (metricas["profit_factor"] >= p["profit_factor_min"] and metricas["expectancy"] > p["expectancy_min"]
            and
            diagnostico["score"] >= p["score_min"]
        ):
            return (
                "La estrategia presenta evidencia objetiva de una "
                "ventaja estadística positiva, mostrando capacidad "
                "para generar valor esperado favorable de forma "
                "consistente."
            )

        return None
    
    def aplicar_regla_F002(self, metricas, diagnostico, evidencia):
        """
        ==========================================================
        REGLA F-002

        Nombre:
            Gestión eficiente del riesgo.

        Dominio:
            Fortalezas Estratégicas.

        Prioridad:
            Alta

        Evidencia utilizada:
            • Reward / Risk
            • Recovery Factor
            • Maximum Drawdown

        Condición:
            Reward / Risk >= 1.50
            Recovery Factor >= 1.00
            Drawdown <= 15 %

        Interpretación:
            La estrategia demuestra una gestión eficiente
            del riesgo, manteniendo controladas las pérdidas
            y una adecuada capacidad de recuperación.

        Decisión que permite tomar:
            Mantener la gestión actual del riesgo como parte
            de la estrategia.

        ==========================================================
        """
        cfg = self.obtener_configuracion_regla("F002")
        p = cfg["parametros"]

        riesgo_ok = (metricas["reward_risk"] >= p["reward_risk_min"])
        recuperacion_ok = (metricas["recovery_factor"] >= p["recovery_factor_min"])
        drawdown_ok = (abs(metricas["max_drawdown"]) <= p["drawdown_max"])

        if (riesgo_ok and recuperacion_ok and drawdown_ok):

            return (
                "La estrategia demuestra una gestión "
                "eficiente del riesgo, manteniendo "
                "controladas las pérdidas y una adecuada "
                "capacidad de recuperación del capital."
            )
        return None

    def aplicar_regla_F003(self, metricas, diagnostico, evidencia):
        """
        ==========================================================
        REGLA F-003

        Nombre:
            Consistencia Operativa.

        Dominio:
            Fortalezas Estratégicas.

        Prioridad:
            Alta

        Evidencia utilizada:
            • Expectancy
            • Recovery Factor
            • Ratio de racha perdedora

        Condición:
            Expectancy >= mínimo
            Recovery Factor >= mínimo
            Ratio de racha perdedora <= máximo

        Interpretación:
            La estrategia demuestra un comportamiento
            operativo consistente y repetible.

        Decisión que permite tomar:
            Considerar la estrategia suficientemente
            estable para continuar su validación.

        ==========================================================
        """

        cfg = self.obtener_configuracion_regla("F003")
        p = cfg["parametros"]

        consistencia_expectancy = (metricas["expectancy"] >= p["expectancy_min"])
        recuperacion_ok = (metricas["recovery_factor"] >= p["recovery_factor_min"])
        racha_ok = (metricas["ratio_racha_perdedora"] <= p["max_ratio_racha_perdedora"])

        if (consistencia_expectancy and recuperacion_ok and racha_ok):

            return (
                "La estrategia presenta una consistencia "
                "operativa adecuada, mostrando un comportamiento "
                "estable y repetible a lo largo de la muestra "
                "analizada."
            )
        
        return None
    
    def aplicar_regla_F004(self, metricas, diagnostico, evidencia):
        """
        REGLA F-004

        Estado:
            Pendiente de implementación.
        """
        return None
    
    def aplicar_regla_F005(self, metricas, diagnostico, evidencia):
        """
        REGLA F-005

        Estado:
            Pendiente de implementación.
        """
        return None
    # --------------------------------------------------

    # ============================================================
    # Evolución del Motor de Hallazgos
    #
    # Iteración 1:
    #     Fortalezas Estratégicas
    #
    # Iteración 2:
    #     Debilidades Estratégicas
    #
    # Iteración 3:
    #     Riesgos
    #
    # Iteración 4:
    #     Oportunidades
    #
    # Iteración 5:
    #     Prioridades
    #
    # Iteración 6:
    #     Conclusión General
    # ============================================================



    # ============================================================
    # 5. PRESENTACIÓN
    # ============================================================
    #
    # Las funciones de esta sección únicamente presentan la
    # información generada por los motores anteriores.
    #
    # No realizan cálculos ni interpretaciones adicionales.
    # ============================================================
    
    def imprimir_resumen(self):
        resumen = self.obtener_resumen()

        print("\n" + "=" * 55)
        print("RESUMEN")
        print("=" * 55)
        for k, v in resumen.items():
            print(f"{k:<25}: {v}")

    # --------------------------------------------------

    def imprimir_long_short(self):

        datos = self.obtener_long_short()

        print("\n" + "=" * 55)
        print("ANÁLISIS LONG vs SHORT")
        print("=" * 55)

        for direccion in ["LONG", "SHORT"]:

            d = datos[direccion]

            print(f"\n{direccion}")

            print(f"{'Operaciones':<20}: {d['total']}")
            print(f"{'Ganadoras':<20}: {d['ganadoras']}")
            print(f"{'Perdedoras':<20}: {d['perdedoras']}")
            print(f"{'Neutras':<20}: {d['neutras']}")
            print(f"{'Win Rate':<20}: {d['win_rate']:.2f}%")
            print(f"{'PnL Total':<20}: {d['pnl']:.2f} USDT")
            print(f"{'ROI Promedio':<20}: {d['roi']:.2f}%")

    # --------------------------------------------------

    def imprimir_estadisticas_simbolos(self):

        datos = self.obtener_estadisticas_simbolos()

        print("\n" + "=" * 85)
        print("ESTADÍSTICAS POR SÍMBOLO")
        print("=" * 85)

        print(f"{'Símbolo':<12}" f"{'Ops':>6}" f"{'Win %':>10}" f"{'PnL':>14}" f"{'ROI %':>12}")
        print("-" * 85)

        for simbolo, d in datos.items():
            print(f"{simbolo:<12}" f"{d['total']:>6}" f"{d['win_rate']:>10.2f}" f"{d['pnl']:>14.2f}" f"{d['roi']:>12.2f}")

    # --------------------------------------------------

    def imprimir_resumen_financiero(self):
        datos = self.obtener_metricas_financieras(self.df_cerradas)

        print("\n" + "=" * 55)
        print("RESUMEN FINANCIERO")
        print("=" * 55)

        print(f"{'Operaciones':<28}: {datos['operaciones']}")

        print()

        print(f"{'Ganancia Bruta':<28}: {datos['ganancia_bruta']:.2f} USDT")
        print(f"{'Pérdida Bruta':<28}: {datos['perdida_bruta']:.2f} USDT")
        print(f"{'PnL Neto':<28}: {datos['pnl_total']:.2f} USDT")

        print()
        print("--------------- DESEMPEÑO ----------------")

        # Profit Factor
        if datos["profit_factor"] == float("inf"):
            pf = "∞"
        else:
            pf = f"{datos['profit_factor']:.2f}"
        print(f"{'Profit Factor':<28}: {pf}")

        # Reward / Risk
        if datos["reward_risk"] == float("inf"):
            rr = "∞"
        else:
            rr = f"{datos['reward_risk']:.2f}"
        print(f"{'Reward / Risk':<28}: {rr}")

        # Recovery Factor
        print(f"{'Recovery Factor':<28}: " f"{datos['recovery_factor']:.2f}")
            
        # Expectancy
        print(f"{'Expectancy':<28}: {datos['expectancy']:.4f} USDT/op")

        print()
        print("--------------- OPERACIONES -------------")

        print(f"{'Promedio Ganancia':<28}: {datos['promedio_ganancia']:.2f} USDT")
        print(f"{'Promedio Pérdida':<28}: {datos['promedio_perdida']:.2f} USDT")
        print(f"{'Mejor Operación':<28}: {datos['mejor_operacion']:.2f} USDT")
        print(f"{'Peor Operación':<28}: {datos['peor_operacion']:.2f} USDT")

        print()
        print("--------------- RETORNO -----------------")

        print(f"{'ROI Promedio':<28}: {datos['roi_promedio']:.2f}%")

    # --------------------------------------------------

    def imprimir_diagnostico(self):
        d = self.obtener_diagnostico()

        print("\n" + "=" * 55)
        print("DIAGNÓSTICO AUTOMÁTICO")
        print("=" * 55)

        print(f"\nScore Estratégico : {d['score']}/100")
        print(f"Clasificación     : {d['nivel']}")

        # print("\nEstado General")
        # print("-" * 55)
        # print(f"Estado General    : {d['estado']}")

        print("\nFortalezas")

        if d["fortalezas"]:
            for item in d["fortalezas"]:
                print(f"✓ {item}")
        else:
            print("-")

        print("\nDebilidades")

        if d["debilidades"]:
            for item in d["debilidades"]:
                print(f"✗ {item}")
        else:
            print("-")

        print("\nObservaciones")

        if d["observaciones"]:
            for item in d["observaciones"]:
                print(f"• {item}")
        else:
            print("-")

        print("\nConclusiones")

        if d["conclusiones"]:
            for item in d["conclusiones"]:
                print(f"► {item}")
        else:
            print("-")

        print("\nRecomendación")

        print(d["recomendacion"])
    # --------------------------------------------------

    def imprimir_evidencia(self):

        e = self.obtener_evidencia()

        print("\n" + "=" * 55)
        print("MOTOR DE EVIDENCIA")
        print("=" * 55)

        if not e:

            print("No existe información suficiente.")
            return

        print(f"{'Mejor símbolo':<32}: " f"{e['mejor_simbolo']} " f"({e['mejor_pnl']:.2f} USDT)")

        print(f"{'Peor símbolo':<32}: " f"{e['peor_simbolo']} " f"({e['peor_pnl']:.2f} USDT)")

        print()

        
        print(f"{'Dirección con mayor PnL':<32}: " f"{e['mejor_direccion']}")

        print(f"{'PnL dirección':<32}: " f"{e['mejor_direccion_pnl']:.2f} USDT")

        print()

        print(f"{'Mayor generador de ganancias (PnL bruto)':<32}: " f"{e['simbolo_mayor_ganancia']}")

        print(f"{'Participación':<32}: " f"{e['aporte_ganancias']:.2f}%")

        print()

        print(f"{'Mayor generador de pérdidas (PnL bruto)':<32}: " f"{e['simbolo_mayor_perdida']}")

        print(f"{'Participación':<32}: " f"{e['aporte_perdidas']:.2f}%")

        print()

        print(f"{'Concentración pérdidas Top2':<32}: " f"{e['drawdown_top2']:.2f}%")

        print()

        print(f"{'Operaciones cerradas':<32}: " f"{e['operaciones']}")

        print(f"{'Muestra suficiente':<32}: " f"{'SI' if e['muestra_suficiente'] else 'NO'}")

        print()

        print(f"{'Versiones detectadas':<32}: " f"{', '.join(e['versiones']) if e['versiones'] else '-'}")

        print(f"{'Modelos Score':<32}: " f"{', '.join(e['score_modelos']) if e['score_modelos'] else '-'}")

        # ---------------------------------------------
        # Top ganancias
        # ---------------------------------------------

        if not e["ganancias"].empty:
            print("\nTop Ganancias")
            for simbolo, pnl in e["ganancias"].head(5).items():
                porcentaje = pnl / e["ganancias"].sum() * 100

                print(f"  {simbolo:<10}" f"{pnl:>8.2f} USDT" f" ({porcentaje:>5.1f}%)")

        # ---------------------------------------------
        # Top pérdidas
        # ---------------------------------------------

        if not e["perdidas"].empty:
            print("\nTop Pérdidas")
            for simbolo, pnl in e["perdidas"].head(5).items():
                porcentaje = pnl / e["perdidas"].sum() * 100

                print(f"  {simbolo:<10}" f"{pnl:>8.2f} USDT" f" ({porcentaje:>5.1f}%)")
   

    def imprimir_resumen_evidencia(self):

        e = self.obtener_evidencia()

        if not e:
            return

        print("\nResumen Ejecutivo de la Evidencia")
        print("-" * 55)

        print(f"• El activo con mejor desempeño es " f"{e['mejor_simbolo']}.")

        print(f"• El activo con peor desempeño es " f"{e['peor_simbolo']}.")

        print(f"• La mejor dirección es " f"{e['mejor_direccion']}.")

        if e["drawdown_top2"] >= 60:

            print(
                "• Las pérdidas están altamente "
                "concentradas en pocos activos."
            )

        elif e["drawdown_top2"] >= 40:

            print(
                "• Existe una concentración moderada "
                "de pérdidas."
            )

        else:

            print(
                "• Las pérdidas se distribuyen de "
                "forma relativamente uniforme."
            )

        if e["muestra_suficiente"]:

            print(
                "• La muestra estadística permite "
                "extraer conclusiones con mayor confianza."
            )

        else:

            print(
                "• Se recomienda continuar recopilando "
                "operaciones antes de modificar la estrategia."
            )
    # --------------------------------------------------

    def imprimir_hallazgos(self):
        metricas = self.obtener_metricas_diagnostico()
        diagnostico = self.obtener_diagnostico()
        evidencia = self.obtener_evidencia()
        hallazgos = self.obtener_hallazgos(metricas, diagnostico, evidencia)

        print("\n" + "=" * 60)
        print("HALLAZGOS ESTRATÉGICOS")
        print("=" * 60)

        print("\nFORTALEZAS ESTRATÉGICAS")

        if hallazgos["fortalezas"]:

            for fortaleza in hallazgos["fortalezas"]:
                print(f"✓ {fortaleza}")

        else:
            print("No se identificaron fortalezas estratégicas.")


    def imprimir_rachas(self):

        datos = self.obtener_rachas()

        print("\n" + "=" * 55)
        print("RACHAS")
        print("=" * 55)

        print(f"{'Máx. Ganadoras':<28}: {datos['max_ganadoras']}")
        print(f"{'Máx. Perdedoras':<28}: {datos['max_perdedoras']}")

        print()

        print(f"{'Racha Actual':<28}: {datos['racha_actual']}")
        print(f"{'Longitud Actual':<28}: {datos['longitud_actual']}")
    # --------------------------------------------------


    def imprimir_curva_capital(self):

        df = self.obtener_curva_capital()

        print("\n" + "=" * 55)
        print("CURVA DE CAPITAL")
        print("=" * 55)

        print(df[["fecha_hora","simbolo", "PnL", "capital"]].tail(10))
    # --------------------------------------------------

    def imprimir_max_drawdown(self):

        datos = self.obtener_max_drawdown()

        print("\n" + "=" * 55)
        print("MÁXIMO DRAWDOWN")
        print("=" * 55)

        print(f"{'Capital Máximo':<25}: {datos['capital_maximo']:.2f} USDT")
        print(f"{'Capital Mínimo':<25}: {datos['capital_minimo']:.2f} USDT")
        print(f"{'Maximum Drawdown':<25}: {datos['max_drawdown']:.2f} USDT")
    #    print(f"{'Drawdown %':<25}: {datos['max_drawdown_pct']:.2f}%")

    # --------------------------------------------------

    # 6. FLUJO PRINCIPAL
    def ejecutar(self):
        self.seleccionar_bot()
        self.cargar_datos()
        self.limpiar_datos()

        self.validar_consistencia()
        
        self.imprimir_resumen()
        self.imprimir_long_short()
        self.imprimir_estadisticas_simbolos()
        self.imprimir_resumen_financiero()
        self.imprimir_diagnostico()
        self.imprimir_evidencia()
        self.imprimir_resumen_evidencia()

        self.imprimir_hallazgos()

        self.imprimir_rachas()
        self.imprimir_curva_capital()
        self.imprimir_max_drawdown()

# =====================================================

# ============================================================
# 6. FLUJO PRINCIPAL
# ============================================================
#
# Flujo oficial del Analizador:
#
# Validación
#      ↓
# Motor Estadístico
#      ↓
# Diagnóstico Automático
#      ↓
# Motor de Evidencia
#      ↓
# Motor de Hallazgos Estratégicos
#      ↓
# Presentación
# ============================================================
def main():
    analizador = AnalizadorEstadisticas()
    analizador.ejecutar()

if __name__ == "__main__":
    main()