#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
ANALIZADOR DE ESTADÍSTICAS
Proyecto Bots Binance

Versión : 1.1
Etapa   : 2
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
    "F004"
)

REGLAS_ACTIVAS = {
    "F001": True,
    "F002": True,
    "F003": True,
    "F004": True,
    "F005": False,
    "F006": False,
    "F007": False,
    "F008": False,
}


REGLAS_DEBILIDADES = (
)

REGLAS_RIESGOS = (
)

REGLAS_PRIORIDADES = (
)

REGLAS_CONCLUSION = (
)


# ==========================================================
# MOTOR DE INVESTIGACIÓN ESTRATÉGICA
# ==========================================================

REGLAS_INVESTIGACION = (
    "I001",
    "I002",
    "I003",
    "I004",
    "I005",
)

REGLAS_INVESTIGACION_ACTIVAS = {
    "I001": True,
    "I002": True,
    "I003": True,
    "I004": True,
    "I005": True,
}

REGLAS_ACTIVAS_CONFIG = {
    "hallazgos": REGLAS_ACTIVAS,
    "investigaciones": REGLAS_INVESTIGACION_ACTIVAS
}

REGLAS_INVESTIGACION_CFG = {

    "I001": {
        "nombre": "Calidad del Score",
        "descripcion":"",
        "prioridad": 1,
        "categoria": "Investigación",
        "version": "1.0",
        "estado":"Implementada",
        "tags":[
            "Score",
            "Clasificación",
            "Optimización"
        ],
    },

    "I002": {
        "nombre": "Rendimiento por símbolo",
        "descripcion":"",
        "prioridad": 2,
        "categoria": "Investigación",
        "version": "1.0",
        "estado":"Implementada",
        "tags":[
            "Score",
            "Clasificación",
            "Optimización"
        ],
    },

    "I003": {
        "nombre": "LONG vs SHORT",
        "descripcion":"",
        "prioridad": 3,
        "categoria": "Investigación",
        "version": "1.0",
        "estado":"Implementada",
        "tags":[
            "Score",
            "Clasificación",
            "Optimización"
        ],
    },

    "I004": {
        "nombre": "Contexto temporal",
        "descripcion":"",
        "prioridad": 4,
        "categoria": "Investigación",
        "version": "1.0",
        "estado":"Implementada",
        "tags":[
            "Score",
            "Clasificación",
            "Optimización"
        ],
    },

    "I005": {
        "nombre": "Calidad del RSI",
        "descripcion":"",
        "prioridad": 5,
        "categoria": "Investigación",
        "version": "1.0",
        "estado":"Implementada",
        "tags":[
            "Score",
            "Clasificación",
            "Optimización"
        ]
    }
}


REGLAS_OPORTUNIDADES = (
)



# ==========================================================
# CONFIGURACIÓN DEL MOTOR DE EVALUACIÓN
# ==========================================================

# ==========================================================
# MOTOR DE EVALUACIÓN DE OPTIMIZACIONES
# ==========================================================
ICO_CRITERIOS = {
    "profit_factor": 1.00,
    "expectancy": 0.00,
    "cobertura": 40.0
}

ICO_CONFIG = {
    "pesos": {
        "profit_factor": 0.40,
        "expectancy": 0.25,
        "win_rate": 0.20,
        "cobertura": 0.15
    }
}   


REGLAS_HALLAZGOS = {
    "F001": {
        "nombre": "Ventaja estadística positiva",
        "codigo": "F001",
        "fuentes": [
            "metricas",
            "diagnostico",
            "evidencia"
        ],
        "descripcion": (
            "Determina si la estrategia demuestra "
            "una ventaja estadística sostenible."
        ),
        "categoria": "Fortaleza",
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "profit_factor_min": 1.00,
            "expectancy_min": 0.00,
            "score_min": 55
        },
        "activo": True,

    },

    "F002": {
        "nombre": "Gestión eficiente del riesgo",
        "codigo": "F002",
        "fuentes": [
            "metricas",
            "diagnostico",
            "evidencia"
        ],
        "descripcion": (
            "Evalúa si la estrategia mantiene una relación "
            "equilibrada entre beneficio, riesgo y "
            "recuperación del capital."
        ),
        "categoria": "Fortaleza",
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "reward_risk_min": 1.50,
            "recovery_factor_min": 1.00,
            "drawdown_max": 15.00
        },
        "activo": True,
    },

    "F003": {
        "nombre": "Consistencia operativa",
        "codigo": "F003",
        "fuentes": [
            "metricas",
            "diagnostico",
            "evidencia"
        ],
        "descripcion": "...",
        "categoria": "Fortaleza",
        "prioridad": "Alta",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {
            "expectancy_min": 0.0,
            "recovery_factor_min": 1.50,
            "max_ratio_racha_perdedora": 0.10
        },
        "activo": True,
    },

    "F004": {
        "nombre": "Diversificación operativa",
        "codigo": "F004",
        "fuentes": [
            "metricas",
            "diagnostico",
            "evidencia"
        ],
        "descripcion": (
            "Evalúa si la rentabilidad de la estrategia se "
            "encuentra adecuadamente distribuida entre los "
            "activos analizados."
        ),
        "categoria": "Fortaleza",
        "prioridad": "Media",
        "estado": "Implementada",
        "version": "1.0",
        "parametros": {

            "aporte_ganancias_max": 40.0,

            "drawdown_top2_max": 60.0

        },
        "activo": True,
    }
}

ESTADO_CUMPLE = "Cumple"
ESTADO_NO_CUMPLE = "No cumple"

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

        # =====================================================
        # Caché de motores
        # =====================================================

        self.metricas = None
        self.metricas_financieras = None
        self.drawdown = None
        self.diagnostico = None
        self.evidencia = None
        self.hallazgos = None
        self.investigaciones = None

        # Nuevos análisis específicos
        self.analisis_score = None
        self.analisis_simbolos = None
        self.analisis_temporal = None
        self.analisis_rsi = None
        self.analisis_long_short = None
        self.curva_capital = None

        self.simulacion_score = None

        self.long_short = None
        self.estadisticas_simbolos = None
        self.rachas = None
        
    # --------------------------------------------------

    # 2. CARGA Y PREPARACIÓN DE DATOS
    def obtener_configuracion_regla(self, codigo):
        """
        Devuelve la configuración oficial de una regla
        del Motor de Hallazgos.
        """
        return REGLAS_HALLAZGOS[codigo]
    
    def crear_hallazgo(self, codigo):
        """
        Construye la estructura estándar utilizada por todas las
        reglas del Motor de Hallazgos Estratégicos.

        Todas las reglas deben devolver este objeto para mantener
        una estructura homogénea y facilitar futuras exportaciones
        (JSON, PDF, Dashboard, API, etc.).
        """

        regla = self.obtener_configuracion_regla(codigo)
        return {
            "codigo": codigo,
            "categoria": regla["categoria"],
            "titulo": regla["nombre"],
            "descripcion": "",
            "estado": "",
            "prioridad": regla["prioridad"],
            "version": regla["version"],
            "valor": None,
            "umbral": regla["parametros"],
            "evidencia": {},
            "recomendacion": ""
        }
    

    """
    Construye la estructura oficial utilizada por
    todas las investigaciones estratégicas.

    Mantiene una estructura homogénea para facilitar
    exportaciones futuras (JSON, Dashboard, API, PDF).
    """
    def crear_investigacion(self, codigo):
        regla = REGLAS_INVESTIGACION_CFG[codigo]
        return {
            "codigo": codigo,
            "titulo": regla["nombre"],
            "categoria": regla["categoria"],
            "prioridad": regla["prioridad"],
            "version": regla["version"],
            "hipotesis": "",
            "objetivo": "",
            "evidencia": {},
            "resultado": self.crear_resultado_investigacion(),
            "conclusion": "",
            "siguiente_paso": "",
            "referencias":[]
        }
    
    def crear_resultado_investigacion(self):
        return {"estado": "Pendiente", "impacto": "", "confianza": "", "metricas": {}}

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

        mdd = self.drawdown["max_drawdown"]

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

        df = self.curva_capital

        if df.empty:
            return {"max_drawdown": 0.0, "capital_maximo": 0.0, "capital_minimo": 0.0}

        # Máximo histórico alcanzado hasta cada operación
        df["capital_max"] = df["capital"].cummax()

        # Drawdown absoluto
        df["drawdown"] = df["capital"] - df["capital_max"]

        mask = df["capital_max"] != 0

        # df.loc[mask, "drawdown_pct"] = (df.loc[mask, "drawdown"] / df.loc[mask, "capital_max"]) * 100

        return {"max_drawdown": df["drawdown"].min(), "capital_maximo": df["capital"].max(),
                "capital_minimo": df["capital"].min()}

    # --------------------------------------------------

    def obtener_rachas(self):
        """
        Calcula las rachas máximas de operaciones
        ganadoras y perdedoras consecutivas.
        """
               
        if self.rachas is not None:
            return self.rachas

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

        self.rachas = {
            "max_ganadoras": max_ganadoras,
            "max_perdedoras": max_perdedoras,
            "racha_actual": nombre[ultima],
            "tipo_actual": ultima,
            "longitud_actual": longitud
        }

        return self.rachas
    
    # --------------------------------------------------

    def obtener_resumen(self):
        return {"Bot": self.nombre_bot, "Archivo": self.archivo.name, "Fecha análisis": self.fecha_analisis.strftime("%Y-%m-%d %H:%M:%S"),
                "Registros": len(self.df), "Operaciones cerradas": len(self.df_cerradas), "Operaciones abiertas": len(self.df_abiertas),
                 "Columnas": len(self.df.columns)}

    # --------------------------------------------------

    def obtener_long_short(self):
        if self.long_short is not None:
            return self.long_short
        direcciones = {}
        for direccion in ["LONG", "SHORT"]:
            df_dir = self.df_cerradas[self.df_cerradas["direccion"] == direccion]
            direcciones[direccion] = self.calcular_metricas(df_dir)
        
        self.long_short = direcciones
        return self.long_short
    
    #    return direcciones
    
    # --------------------------------------------------

    def obtener_estadisticas_simbolos(self):
        """
        Calcula las estadísticas de cada símbolo.
        """
        if self.estadisticas_simbolos is not None:
            return self.estadisticas_simbolos

        estadisticas = {}
        simbolos = sorted(self.df_cerradas["simbolo"].unique())
        for simbolo in simbolos:
            df_simbolo = self.df_cerradas[self.df_cerradas["simbolo"] == simbolo]
            estadisticas[simbolo] = self.calcular_metricas(df_simbolo)
        self.estadisticas_simbolos = estadisticas

        return self.estadisticas_simbolos   
    #    return estadisticas

    # --------------------------------------------------

    # --------------------------------------------------
    # 3.3 Herramientas de Segmentación Estadística
    # -------------------------------------------------
    def obtener_analisis_segmentado(self, campo, segmentos=None):
        """
        Genera un análisis estadístico segmentado para
        cualquier variable del dataset.

        Si 'segmentos' es None, el análisis se realiza
        por categorías (ej.: símbolo, dirección).

        Si 'segmentos' contiene límites numéricos,
        se agrupa por rangos.
        """

        if self.df_cerradas.empty:
            return {"campo": campo, "total_operaciones": 0, "segmentos": {}
            }

        df = self.df_cerradas.copy()

        # ------------------------------------------
        # Segmentación
        # ------------------------------------------
        if segmentos is not None:
            etiquetas = []
            for i in range(len(segmentos) - 1):
                etiquetas.append(f"{segmentos[i]}-{segmentos[i+1]-1}")

            df["_grupo"] = pd.cut(df[campo], bins=segmentos, labels=etiquetas, include_lowest=True, right=False)

        else:
            df["_grupo"] = df[campo]

        resultado = {"campo": campo, "total_operaciones": len(df), "segmentos": {}}

        # ------------------------------------------
        # Estadísticas
        # ------------------------------------------

        for grupo, datos in df.groupby("_grupo", observed=False):
            if len(datos) == 0:
                continue

            pnl = datos["PnL"]

            ganadoras = pnl[pnl > 0]
            perdedoras = pnl[pnl < 0]

            ganancia_bruta = ganadoras.sum()
            perdida_bruta = abs(perdedoras.sum())

            if perdida_bruta > 0:
                profit_factor = ganancia_bruta / perdida_bruta
            else:
                profit_factor = float("inf")

            promedio_ganancia = (
                ganadoras.mean()
                if len(ganadoras)
                else 0
            )

            promedio_perdida = (
                abs(perdedoras.mean())
                if len(perdedoras)
                else 0
            )

            reward_risk = (
                promedio_ganancia / promedio_perdida
                if promedio_perdida > 0
                else float("inf")
            )

            resultado["segmentos"][str(grupo)] = {
                "operaciones": len(datos),
                "ganadoras": int((pnl > 0).sum()),
                "perdedoras": int((pnl < 0).sum()),
                "win_rate":
                    round((pnl > 0).mean() * 100, 2),
                "profit_factor":
                    round(profit_factor, 2),
                "expectancy":
                    round(pnl.mean(), 4),
                "reward_risk":
                    round(reward_risk, 2),
                "roi":
                    round(datos["ROI"].mean(), 2),
                "pnl":
                    round(pnl.sum(), 2)
            }

        return resultado

    def obtener_analisis_score(self):
        """
        Devuelve el análisis segmentado del Score.

        El resultado queda almacenado en caché para
        evitar recálculos durante la ejecución.
        """

        if self.analisis_score is not None:
            return self.analisis_score

        self.analisis_score = (
            self.obtener_analisis_segmentado(
                campo="score",
                segmentos=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 101]
            )
        )

        return self.analisis_score

    # --------------------------------------------------
    # 3.4 HERRAMIENTAS DE SIMULACIÓN
    # --------------------------------------------------
    def simular_umbral_minimo(self, campo, umbral):
        """
        Simula el comportamiento de la estrategia
        eliminando todas las operaciones cuyo
        valor del campo sea inferior al umbral.
        """

        df = self.df_cerradas.copy()
        df = df[df[campo] >= umbral]
        operaciones = len(df)

        if operaciones == 0:
            return None

        pnl = df["PnL"]
        ganancias = pnl[pnl > 0]
        perdidas = pnl[pnl < 0]
        ganancia_bruta = ganancias.sum()

        perdida_bruta = abs(perdidas.sum())

        profit_factor = (
            ganancia_bruta / perdida_bruta
            if perdida_bruta > 0
            else float("inf")
        )

        expectancy = pnl.mean()

        win_rate = ((pnl > 0).mean() * 100)

        roi = df["ROI"].mean()

        return {
            "umbral": umbral,
            "operaciones": operaciones,
            "cobertura":
                round(operaciones / len(self.df_cerradas)*100, 2),

            "profit_factor":
                round(profit_factor, 2),

            "expectancy":
                round(expectancy, 4),

            "win_rate":
                round(win_rate, 2),

            "roi":
                round(roi, 2)

        }

    def obtener_simulacion_score(self):
        if self.simulacion_score is not None:
            return self.simulacion_score
        simulaciones = []
        for umbral in range(20,91,5):
            r = self.simular_umbral_minimo("score", umbral)

            if r:
                simulaciones.append(r)

        self.simulacion_score = simulaciones

        return simulaciones

   
    # --------------------------------------------------
    # 3.3 Diagnóstico Automático
    # --------------------------------------------------

    def obtener_metricas_diagnostico(self):
        """
        Reúne todas las métricas necesarias para el
        Diagnóstico Automático.

        No interpreta resultados.
        No imprime información.
        Únicamente centraliza las métricas calculadas
        por otros métodos.
        """

    #    financieras = self.obtener_metricas_financieras(self.df_cerradas)
        financieras = self.metricas_financieras
        drawdown = self.drawdown
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

        if m is None:
            raise ValueError(
                "obtener_metricas_diagnostico() devolvió None."
        )

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

    def obtener_diagnostico(self, metricas=None): 
    # def obtener_diagnostico(self):
        """
        Interpreta de forma integrada las métricas
        calculadas por el analizador.

        El objetivo no es evaluar indicadores aislados,
        sino identificar las posibles causas del
        desempeño de la estrategia.
        """
        if metricas is None:
            metricas = self.obtener_metricas_diagnostico()

        score = self.obtener_score_estrategico(metricas)
        m = metricas

    #    m = self.obtener_metricas_diagnostico()

    #    score = self.obtener_score_estrategico(m)

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
        # ======================================
        # Evidencia general
        # ======================================

        # ======================================
        # Evidencia por símbolo
        # ======================================

        # ======================================
        # Evidencia direccional
        # ======================================

        # ======================================
        # Evidencia operacional
        # ======================================




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
            "debilidades": self.obtener_debilidades_estrategicas(),
            "riesgos": self.obtener_riesgos_estrategicos(),
            "oportunidades": self.obtener_oportunidades_estrategicas(),
            "prioridades": self.obtener_prioridades_estrategicas(),
            "conclusion_general": self.obtener_conclusion_general()
        }

        return hallazgos

    def ejecutar_reglas(self, lista_reglas, reglas_activas, metricas, diagnostico, evidencia):
        resultados = []
        for codigo in lista_reglas:
            if not reglas_activas.get(codigo, False):
                continue

            regla = getattr(self, f"aplicar_regla_{codigo}", None)

            if regla is None:
                continue

            resultado = regla(metricas, diagnostico, evidencia)

            if resultado:
                resultados.append(resultado)

        return resultados

    def obtener_fortalezas_estrategicas(self, metricas, diagnostico, evidencia):
        """
        Ejecuta todas las reglas registradas
        para Fortalezas Estratégicas.
        """
        return self.ejecutar_reglas(
            REGLAS_FORTALEZAS,
            REGLAS_ACTIVAS,
            metricas,
            diagnostico,
            evidencia
        )


    def obtener_debilidades_estrategicas(self):
        return []

    def obtener_riesgos_estrategicos(self):
        return []

    def obtener_oportunidades_estrategicas(self):
        return []

    def obtener_prioridades_estrategicas(self):
        return []

    def obtener_conclusion_general(self):
        return []


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
        cfg = self.obtener_configuracion_regla("F001")
        p = cfg["parametros"]

        if (metricas["profit_factor"] >= p["profit_factor_min"] and metricas["expectancy"] > p["expectancy_min"]
            and
            diagnostico["score"] >= p["score_min"]
        ):
            
            hallazgo = self.crear_hallazgo("F001")
            hallazgo["descripcion"] = (
                "La estrategia presenta evidencia objetiva de una "
                "ventaja estadística positiva, mostrando capacidad "
                "para generar valor esperado favorable de forma "
                "consistente."
            )

            hallazgo["estado"] = ESTADO_CUMPLE
            hallazgo["valor"] = {
                "profit_factor": metricas["profit_factor"],
                "expectancy": metricas["expectancy"],
                "score": diagnostico["score"]
            }
            hallazgo["umbral"] = p
            hallazgo["recomendacion"] = (
                "Continuar la validación estadística antes de "
                "realizar optimizaciones importantes."
            )
            return hallazgo

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

        if riesgo_ok and recuperacion_ok and drawdown_ok:

            hallazgo = self.crear_hallazgo("F002")

            hallazgo["descripcion"] = (
                "La estrategia demuestra una gestión eficiente "
                "del riesgo, manteniendo controladas las pérdidas "
                "y una adecuada capacidad de recuperación."
            )

            hallazgo["estado"] = ESTADO_CUMPLE

            hallazgo["valor"] = {
                "reward_risk": metricas["reward_risk"],
                "recovery_factor": metricas["recovery_factor"],
                "max_drawdown": metricas["max_drawdown"]
            }

            hallazgo["umbral"] = p
            hallazgo["recomendacion"] = (
                "Mantener la política actual de gestión de riesgo."
            )

            return hallazgo
        
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
        racha_ok = (metricas["ratio_racha_perdedora"] <= p["max_ratio_racha_perdedora"]
        )

        if (consistencia_expectancy and recuperacion_ok and racha_ok):

            hallazgo = self.crear_hallazgo("F003")

            hallazgo["descripcion"] = (
                "La estrategia presenta un comportamiento operativo "
                "consistente y repetible durante la muestra analizada."
            )

            hallazgo["estado"] = ESTADO_CUMPLE

            hallazgo["valor"] = {
                "expectancy": metricas["expectancy"],
                "recovery_factor": metricas["recovery_factor"],
                "ratio_racha": metricas["ratio_racha_perdedora"]
            }

            hallazgo["umbral"] = p

            hallazgo["recomendacion"] = (
                "Continuar aumentando la muestra estadística para "
                "confirmar la estabilidad observada."
            )

            return hallazgo
        
        return None
    
    def aplicar_regla_F004(self, metricas, diagnostico, evidencia):
        """
        ==========================================================
        REGLA F-004

        Nombre:
            Diversificación Operativa.

        Dominio:
            Fortalezas Estratégicas.

        Prioridad:
            Media

        Evidencia utilizada:
            • Aporte de ganancias del mejor activo.
            • Concentración de pérdidas Top-2.

        Condición:
            Aporte ganancias <= máximo permitido.
            Concentración pérdidas <= máximo permitido.

        Interpretación:
            La estrategia distribuye su desempeño entre
            varios activos, reduciendo la dependencia de
            casos individuales.

        Decisión que permite tomar:
            Mantener la selección actual de activos
            como una base suficientemente diversificada.
        ==========================================================
        """

        cfg = self.obtener_configuracion_regla("F004")
        p = cfg["parametros"]

        ganancias_ok = (evidencia["aporte_ganancias"] <= p["aporte_ganancias_max"])

        perdidas_ok = (evidencia["drawdown_top2"] <= p["drawdown_top2_max"])

        if ganancias_ok and perdidas_ok:
            hallazgo = self.crear_hallazgo("F004")
            hallazgo["descripcion"] = (
                "La estrategia presenta una adecuada "
                "diversificación operativa, evitando una "
                "dependencia excesiva de pocos activos."
            )

            hallazgo["estado"] = ESTADO_CUMPLE
            hallazgo["valor"] = {
                "aporte_ganancias":
                    evidencia["aporte_ganancias"],

                "drawdown_top2":
                    evidencia["drawdown_top2"]
            }

            hallazgo["recomendacion"] = (
                "Mantener la composición actual del universo "
                "de activos mientras continúe mostrando un "
                "comportamiento equilibrado."
            )

            return hallazgo

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

    # ==========================================================
    # MOTOR DE EVALUACIÓN DE OPTIMIZACIONES
    # ==========================================================


    # ============================================================
    # 4.4 MOTOR DE EVALUACIÓN DE OPTIMIZACIONES (ICO)
    # ============================================================
    def calcular_ico(self, simulacion):
        """
        Calcula el Índice de Calidad de Optimización
        (ICO) para una propuesta de mejora.

        Este índice permite comparar distintas
        optimizaciones utilizando un criterio
        multicriterio homogéneo.
        """

        pesos = ICO_CONFIG["pesos"]
        for campo in ("pf_norm", "exp_norm", "wr_norm", "cobertura_norm"):

            if campo not in simulacion:
                raise ValueError(
                    f"No existe {campo}."
                )

        return round(
            simulacion["pf_norm"]
            * pesos["profit_factor"]
            +
            simulacion["exp_norm"]
            * pesos["expectancy"]
            +
            simulacion["wr_norm"]
            * pesos["win_rate"]
            +
            simulacion["cobertura_norm"]
            * pesos["cobertura"]
            ,
            4
        )
    
    def obtener_restricciones_ico(self):
        """
        Calcula automáticamente las restricciones mínimas
        para aceptar una simulación.

        Las restricciones crecen junto con el tamaño
        de la muestra estadística.
        """

        total = len(self.df_cerradas)

        min_operaciones = max(15, round(total * 0.15))

        min_cobertura = max(15, round(total * 0.15))

        return {
            "min_operaciones": min_operaciones,
            "min_cobertura": min_cobertura
        }

    def normalizar_minmax(self, valor, minimo, maximo):
        """
        Normalización Min-Max.
        """

        if maximo == minimo:
            return 1.0

        return ((valor - minimo) / (maximo - minimo))

    # --------------------------------------------------
    # Evaluación multicriterio
    # --------------------------------------------------
    def evaluar_optimizaciones(self, simulaciones):
        """
        Evalúa las simulaciones mediante un índice
        multicriterio configurable.
        """

        restricciones = self.obtener_restricciones_ico()
        simulaciones = [
            s
            for s in simulaciones
            if (s["operaciones"] >= restricciones["min_operaciones"]
                and
                s["cobertura"] >= restricciones["min_cobertura"]
            )
        ]

        if not simulaciones:
            return None

        # max_pf = max(s["profit_factor"] for s in simulaciones)
        # max_wr = max(s["win_rate"] for s in simulaciones)
        # max_exp = max(s["expectancy"] for s in simulaciones)

        # ------------------------------------------------- 
        # Valores extremos para normalización Min-Max
        # -------------------------------------------------

        pf_vals = [s["profit_factor"] for s in simulaciones if s["profit_factor"] != float("inf")]

        if not pf_vals:
            pf_vals = [1]
        pf_min = min(pf_vals)
        pf_max = max(pf_vals)

        exp_vals = [s["expectancy"] for s in simulaciones]
        exp_min = min(exp_vals)
        exp_max = max(exp_vals)

        wr_vals = [s["win_rate"] for s in simulaciones]
        wr_min = min(wr_vals)
        wr_max = max(wr_vals)

        cobertura_vals = [s["cobertura"] for s in simulaciones]
        cobertura_min = min(cobertura_vals)
        cobertura_max = max(cobertura_vals)

        for s in simulaciones:
            # -----------------------------------------
            # Profit Factor
            # -----------------------------------------

            # if s["profit_factor"] == float("inf"):
            #     pf = 1.0

            # elif pf_max == pf_min:
            #     pf = 1.0

            # else:
            #     pf = ((s["profit_factor"] - pf_min) / (pf_max - pf_min))

            if s["profit_factor"] == float("inf"):
                pf = 1.0
            else:
                pf = self.normalizar_minmax(
                    s["profit_factor"],
                    pf_min,
                    pf_max
    )

            # -----------------------------------------
            # Expectancy
            # -----------------------------------------

            # if exp_max == exp_min:
            #     exp = 1.0

            # else:
            #     exp = ((s["expectancy"] - exp_min) / (exp_max - exp_min))
            exp = self.normalizar_minmax(s["expectancy"], exp_min, exp_max)

            # -----------------------------------------
            # Win Rate
            # -----------------------------------------

            # if wr_max == wr_min:
            #     wr = 1.0

            # else:
            #     wr = ((s["win_rate"] - wr_min) / (wr_max - wr_min))
            wr = self.normalizar_minmax(s["win_rate"], wr_min, wr_max)

            # -----------------------------------------
            # Cobertura
            # -----------------------------------------

            # if cobertura_max == cobertura_min:
            #     cobertura  = 1.0

            # else:
            #     cobertura  = ((s["cobertura"] - cobertura_min) / (cobertura_max - cobertura_min))
            cobertura = self.normalizar_minmax(s["cobertura"], cobertura_min, cobertura_max)

            s["pf_norm"] = pf
            s["wr_norm"] = wr
            s["exp_norm"] = exp
            s["cobertura_norm"] = cobertura 

            s["ico"] = self.calcular_ico(s)

        return max(simulaciones, key=lambda x: x["ico"])


    # ============================================================
    # 4.4 MOTOR DE INVESTIGACIÓN ESTRATÉGICA
    # ============================================================
    # ============================================================
    # FILOSOFÍA DEL MOTOR DE INVESTIGACIÓN
    #
    # Este motor NO modifica estrategias.
    #
    # Su única responsabilidad es generar hipótesis de
    # investigación priorizadas y sustentadas por evidencia
    # estadística.
    #
    # La decisión de modificar el bot siempre pertenece
    # al proceso de Optimización Basada en Evidencia.
    # ============================================================
    def obtener_investigaciones(self, metricas, diagnostico, evidencia):

        investigaciones = self.ejecutar_reglas(
            REGLAS_INVESTIGACION,
            REGLAS_INVESTIGACION_ACTIVAS,
            metricas,
            diagnostico,
            evidencia
        )

        investigaciones.sort(
            key=lambda x: x["prioridad"]
        )

        return investigaciones

    # ------------------------------------------------------------
    # Herramientas específicas de investigación
    # ------------------------------------------------------------
    # ==========================================================
    # Evidencia específica de la investigación I001
    #
    # No pertenece al Motor de Evidencia Global.
    # Consume únicamente información relacionada
    # con la investigación del Score.
    # ==========================================================
    def obtener_evidencia_score(self):
        """
        Integra la evidencia obtenida del análisis
        segmentado y de la simulación de umbrales.
        """

        analisis = self.obtener_analisis_score()
        simulaciones = self.obtener_simulacion_score()  

        segmentos = analisis["segmentos"]

        if not segmentos:
            return {}

        # Mejor y peor segmento según Profit Factor
        mejor_segmento = max(segmentos.items(), key=lambda x: x[1]["profit_factor"])

        peor_segmento = min(segmentos.items(), key=lambda x: x[1]["profit_factor"])

        # -----------------------------
        # Mejor simulación
        # -----------------------------

        simulaciones_validas = [
            s for s in simulaciones
            if s is not None
        ]

        if simulaciones_validas:
            mejor_simulacion = self.evaluar_optimizaciones(simulaciones)
        else:
            mejor_simulacion = None

        estado = (
            "Con evidencia"
            if mejor_simulacion is not None
            else "Sin evidencia"
        )

        if mejor_simulacion is None:
            return {

                "estado": estado,

                "mejor_rango": mejor_segmento[0],
                "peor_rango": peor_segmento[0],

                "mejor_pf_segmento":
                    mejor_segmento[1]["profit_factor"],

                "peor_pf_segmento":
                    peor_segmento[1]["profit_factor"],

                "mejor_umbral": None,
                "mejor_pf": None,
                "expectancy": None,
                "win_rate": None,
                "roi": None,
                "cobertura": None,
                "operaciones": 0,
                "ico": 0,

                "total_operaciones":
                    analisis["total_operaciones"]
            }

        return {

            # ==========================
            # Evidencia análisis
            # ==========================

            "mejor_rango": mejor_segmento[0],
            "peor_rango": peor_segmento[0],
            "mejor_pf_segmento":
                mejor_segmento[1]["profit_factor"],
            "peor_pf_segmento":
                peor_segmento[1]["profit_factor"],

            # ==========================
            # Evidencia simulación
            # ==========================

            "mejor_umbral":
                mejor_simulacion["umbral"]
                if mejor_simulacion else None,

            "mejor_pf":
                mejor_simulacion["profit_factor"]
                if mejor_simulacion else None,

            "expectancy":
                mejor_simulacion["expectancy"]
                if mejor_simulacion else None,

            "win_rate":
                mejor_simulacion["win_rate"]
                if mejor_simulacion else None,

            "roi":
                mejor_simulacion["roi"]
                if mejor_simulacion else None,

            "cobertura":
                mejor_simulacion["cobertura"]
                if mejor_simulacion else None,

            "operaciones":
                mejor_simulacion["operaciones"]
                if mejor_simulacion else None,

            # ==========================
            # General
            # ==========================

            "total_operaciones":
                analisis["total_operaciones"],

            "ico":
                mejor_simulacion["ico"]
                if mejor_simulacion else None,
        }
    
    def obtener_conclusion_score(self):
        """
        Genera una conclusión automática a partir
        de la evidencia obtenida.
        """

        e = self.obtener_evidencia_score()

        if e.get("estado") == "Sin evidencia":
            return (
                "No existe evidencia estadística suficiente "
                "para recomendar un cambio en el Score."
            )

        if (e["mejor_pf"] < ICO_CRITERIOS["profit_factor"]):
            return (
                "No existe evidencia suficiente "
                "para modificar el Score."
            )

        if (e["cobertura"] < ICO_CRITERIOS["cobertura"]):
            return (
                "El mejor umbral reduce "
                "excesivamente la cobertura. "
                "No es recomendable."
            )

        return (f"Existe evidencia para elevar " f"el Score mínimo a " f"{e['mejor_umbral']}.")

    def obtener_recomendacion_score(self):
        """
        Genera una recomendación preliminar basada
        en la evidencia del Score.
        """

        e = self.obtener_evidencia_score()

        if e.get("estado") == "Sin evidencia":
            return (
                "Continuar recopilando operaciones."
            )

        if (e["mejor_pf"] < ICO_CRITERIOS["profit_factor"]):
            return (
                "Continuar recopilando datos."
            )

        if (e["cobertura"] < ICO_CRITERIOS["cobertura"]):
            return (
                "Esperar una cobertura "
                "estadística mayor."
            )

        return (f"Simular la estrategia " f"utilizando Score ≥ " f"{e['mejor_umbral']}.")

    def aplicar_regla_I001(self, metricas, diagnostico,  evidencia):

        inv = self.crear_investigacion("I001")

        inv["hipotesis"] = (
            "El Score actual discrimina las mejores "
            "oportunidades de trading."
        )

        inv["objetivo"] = (
            "Validar estadísticamente la capacidad "
            "predictiva del Score."
        )

        inv["evidencia"] = (
            self.obtener_evidencia_score()
        )

        inv["conclusion"] = (
            self.obtener_conclusion_score()
        )

        inv["siguiente_paso"] = (
            self.obtener_recomendacion_score()
        )

        # inv["evidencia"].get("estado")
        inv["resultado"]["impacto"] = "Muy Alto"
        inv["resultado"]["confianza"] = "Media"

        inv["resultado"]["metricas"] = {

            "analisis":
                self.obtener_analisis_score(),

            "simulacion":
                self.obtener_simulacion_score()
        }

        # if inv["evidencia"]["estado"] == "Sin evidencia":
        if inv["evidencia"].get("estado") == "Sin evidencia":
            inv["resultado"]["estado"] = "Pendiente"
            inv["resultado"]["confianza"] = "Insuficiente"
            return inv

        ico = inv["evidencia"]["ico"]

        cobertura = inv["evidencia"]["cobertura"]
        if ico >= 0.85 and cobertura >= 70:
            confianza = "Muy Alta"
        elif ico >= 0.70 and cobertura >= 60:
            confianza = "Alta"
        elif ico >= 0.55 and cobertura >= 45:
            confianza = "Media"
        else:
            confianza = "Baja"

        inv["resultado"]["confianza"] = confianza

        return inv

    # =====================================================
    # ORDEN OFICIAL DE EJECUCIÓN DE LOS MOTORES
    # =====================================================
    def inicializar_motores(self):
        """
        Ejecuta una única vez todos los motores del analizador.

        El objetivo es evitar recalcular información durante
        la etapa de presentación.

        Todas las funciones de impresión deberán consumir
        exclusivamente estos resultados.
        """
        self.curva_capital = self.obtener_curva_capital()
        self.drawdown = self.obtener_max_drawdown()
        self.metricas_financieras = (self.obtener_metricas_financieras(self.df_cerradas))

        self.metricas = self.obtener_metricas_diagnostico()
    #    self.diagnostico = self.obtener_diagnostico()
        self.diagnostico = self.obtener_diagnostico(self.metricas)
        self.evidencia = self.obtener_evidencia()
    #    self.evidencia = self.obtener_evidencia(self.metricas)

        self.hallazgos = self.obtener_hallazgos(self.metricas, self.diagnostico, self.evidencia)
        self.investigaciones = self.obtener_investigaciones(self.metricas, self.diagnostico, self.evidencia)



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
    #    datos = self.obtener_metricas_financieras(self.df_cerradas)
        datos = self.metricas_financieras

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
        d = self.diagnostico

        print("\n" + "=" * 55)
        print("DIAGNÓSTICO AUTOMÁTICO")
        print("=" * 55)

        print(f"\nScore Estratégico : {d['score']}/100")
        print(f"Clasificación     : {d['nivel']}")

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

        e = self.evidencia

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

        e = self.evidencia

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
        hallazgos = self.hallazgos

        print("\n" + "=" * 60)
        print("HALLAZGOS ESTRATÉGICOS")
        print("=" * 60)

        print("\nFORTALEZAS ESTRATÉGICAS")

        if hallazgos["fortalezas"]:

            for h in hallazgos["fortalezas"]:
                print(f"\n✓ {h['codigo']} - {h['titulo']}")

                print(f"  Estado        : {h['estado']}")
                print(f"  Prioridad     : {h['prioridad']}")
                print(f"  Versión       : {h['version']}")
                print(f"  Descripción   : {h['descripcion']}")
                print(f"  Recomendación : {h['recomendacion']}")

        else:
            print("No se identificaron fortalezas estratégicas.")

    def imprimir_investigaciones(self):
        investigaciones = self.investigaciones

        print("\n")
        print("=" * 60)
        print("PLAN DE INVESTIGACIÓN")
        print("=" * 60)

        for inv in investigaciones:
            print(f"\n{inv['codigo']} - {inv['titulo']}")
            print(f"Prioridad      : {inv['prioridad']}")
            print(f"Hipótesis      : {inv['hipotesis']}")
            print(f"Objetivo       : {inv['objetivo']}")
            print(f"Siguiente paso : {inv['siguiente_paso']}")


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

        df = self.curva_capital

        print("\n" + "=" * 55)
        print("CURVA DE CAPITAL")
        print("=" * 55)

        print(df[["fecha_hora","simbolo", "PnL", "capital"]].tail(10))
    # --------------------------------------------------

    def imprimir_max_drawdown(self):

    #    datos = self.obtener_max_drawdown()
        datos = self.drawdown

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

        # =====================================
        # Inicialización única de motores
        # =====================================
        self.inicializar_motores()
        
        # =====================================
        # Presentación
        # =====================================
        self.imprimir_resumen()
        self.imprimir_long_short()
        self.imprimir_estadisticas_simbolos()
        self.imprimir_resumen_financiero()
        self.imprimir_diagnostico()
        self.imprimir_evidencia()
        self.imprimir_resumen_evidencia()

        self.imprimir_hallazgos()
        self.imprimir_investigaciones()

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