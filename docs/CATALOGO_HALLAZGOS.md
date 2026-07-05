# CATALOGO_HALLAZGOS.md

Versión: 1.0

Proyecto:
Bots Binance

Documento:
Base Oficial de Conocimiento del Motor de Hallazgos Estratégicos

Estado:
En desarrollo

Última actualización:
Julio 2026

---

# 1. Objetivo

El presente documento constituye la Base Oficial de Conocimiento del Motor de Hallazgos Estratégicos del Analizador de Estadísticas.

Su propósito es documentar el conocimiento metodológico utilizado para transformar métricas objetivas en conclusiones estratégicas.

Este documento define:

- los dominios de conocimiento que interpreta el Analizador;
- la clasificación oficial de las reglas;
- las convenciones metodológicas;
- el estado de implementación de cada regla.

El código fuente implementa estas reglas.

Este documento describe su significado y finalidad.

---

# 2. Alcance

El Catálogo de Hallazgos forma parte del Analizador de Estadísticas del Proyecto Bots Binance.

Su función es servir como referencia metodológica para todas las versiones futuras del Analizador.

Toda nueva regla deberá documentarse previamente en este catálogo antes de incorporarse al código.

---

# 3. Filosofía del Motor de Hallazgos

El Motor de Hallazgos no constituye un sistema basado en Inteligencia Artificial.

Es un motor de inferencia basado en reglas explícitas, reproducibles y sustentadas exclusivamente por evidencia estadística.

Su finalidad no es calcular indicadores.

Los indicadores ya han sido calculados por el Motor Estadístico.

Su finalidad consiste en interpretar conjuntamente dichas evidencias para producir conocimiento estratégico útil para la evolución de las estrategias.

---

# 4. Principios Metodológicos

Toda regla deberá respetar obligatoriamente los siguientes principios.

## Dependencias Permitidas

Las reglas únicamente podrán utilizar información proveniente de:

- Motor Estadístico
- Diagnóstico Automático
- Motor de Evidencia

Una regla nunca podrá depender del resultado de otra regla.

Todas las reglas deberán ser completamente independientes.

## 4.1 Independencia

Cada regla constituye una unidad independiente.

Una regla podrá modificarse, incorporarse o eliminarse sin afectar el funcionamiento del resto del sistema.

---

## 4.2 Reproducibilidad

La misma información de entrada deberá generar exactamente el mismo hallazgo.

El Motor de Hallazgos nunca deberá introducir elementos aleatorios ni interpretaciones subjetivas.

---

## 4.3 Evidencia

Toda regla deberá construirse exclusivamente utilizando información proveniente de:

- Motor Estadístico.
- Diagnóstico Automático.
- Motor de Evidencia.

Las reglas nunca recalcularán indicadores.

---

## 4.4 No Redundancia

Dos reglas diferentes no deberán generar el mismo conocimiento.

Cada regla deberá aportar una interpretación distinta.

---

## 4.5 Interpretación

Una regla no interpreta una métrica aislada.

Una regla interpreta la relación existente entre múltiples evidencias.

Por esta razón una regla podrá utilizar uno o varios indicadores simultáneamente.

---

## 4.6 Modularidad

Las reglas deberán implementarse como componentes independientes.

El orden de ejecución nunca deberá modificar el resultado final.

---

# 5. Convenciones Oficiales

Las reglas se identifican mediante un código permanente.

Formato oficial:

F001

D001

R001

O001

P001

C001

Cada identificador es único.

Un identificador nunca deberá reutilizarse.

Las reglas eliminadas conservarán su código como parte del historial metodológico del proyecto.

---

# 6. Base Oficial de Conocimiento

El conocimiento del Analizador se organiza en seis dominios estratégicos.

Cada dominio responde a una pregunta diferente.

| Grupo | Pregunta |
|---------|----------|
| F | ¿Qué hace bien la estrategia? |
| D | ¿Qué limita actualmente su rendimiento? |
| R | ¿Qué podría deteriorar su desempeño futuro? |
| O | ¿Dónde existe mayor potencial de mejora? |
| P | ¿Qué debería hacerse primero? |
| C | ¿Qué aprendimos de esta estrategia? |

# 6.1 Jerarquía de las Reglas

No todas las reglas poseen la misma importancia metodológica.

Cada regla pertenece a uno de los siguientes niveles.

| Nivel | Descripción |
|--------|-------------|
| Alta | Influye directamente en la evaluación global de la estrategia. |
| Media | Complementa la interpretación principal. |
| Baja | Aporta contexto adicional sin modificar la conclusión global. |

La prioridad metodológica no determina el orden de ejecución.

Determina únicamente la relevancia del conocimiento generado.

---

# 7. Catálogo Oficial de Reglas

## 7.1 Fortalezas Estratégicas (F)

Las Fortalezas representan capacidades demostradas por la estrategia mediante evidencia objetiva.

Su finalidad consiste en identificar aquellos aspectos que contribuyen positivamente al desempeño global.

| Código | Dominio | Estado |
|----------|----------|---------|
| F001 | Ventaja estadística | ✅ Implementada |
| F002 | Gestión eficiente del riesgo | ✅ Implementada |
| F003 | Consistencia operativa | ⏳ Pendiente |
| F004 | Diversificación del rendimiento | ⏳ Pendiente |
| F005 | Calidad de la muestra | ⏳ Pendiente |
| F006 | Robustez de la estrategia | ⏳ Pendiente |
| F007 | Estabilidad temporal | ⏳ Pendiente |
| F008 | Calidad de ejecución | ⏳ Pendiente |
| F009 | Reserva estratégica | Disponible |

---

## 7.2 Debilidades Estratégicas (D)

Las Debilidades representan limitaciones comprobadas que reducen el desempeño actual de la estrategia.

| Código | Dominio | Estado |
|----------|----------|---------|
| D001 | Ausencia de ventaja estadística | ⏳ Pendiente |
| D002 | Gestión deficiente del riesgo | ⏳ Pendiente |
| D003 | Baja consistencia | ⏳ Pendiente |
| D004 | Dependencia de activos | ⏳ Pendiente |
| D005 | Dependencia LONG / SHORT | ⏳ Pendiente |
| D006 | Evidencia insuficiente | ⏳ Pendiente |
| D007 | Drawdown elevado | ⏳ Pendiente |
| D008 | Inestabilidad temporal | ⏳ Pendiente |
| D009 | Reserva estratégica | Disponible |

---

## 7.3 Riesgos (R)

Los Riesgos representan factores que podrían comprometer el desempeño futuro de la estrategia.

| Código | Dominio | Estado |
|----------|----------|---------|
| R001 | Riesgo por concentración | ⏳ Pendiente |
| R002 | Riesgo por rachas | ⏳ Pendiente |
| R003 | Riesgo por muestra limitada | ⏳ Pendiente |
| R004 | Riesgo de sobreoptimización | ⏳ Pendiente |
| R005 | Riesgo de mercado | ⏳ Pendiente |
| R006 | Riesgo de deterioro | ⏳ Pendiente |
| R007 | Riesgo operacional | ⏳ Pendiente |
| R008 | Riesgo por transición de versiones | ⏳ Pendiente |
| R009 | Reserva estratégica | Disponible |

---

## 7.4 Oportunidades (O)

Las Oportunidades representan áreas con potencial de mejora identificado mediante evidencia objetiva.

| Código | Dominio | Estado |
|----------|----------|---------|
| O001 | Incrementar la ventaja estadística | ⏳ Pendiente |
| O002 | Mejorar la eficiencia del riesgo | ⏳ Pendiente |
| O003 | Optimizar selección de activos | ⏳ Pendiente |
| O004 | Equilibrar LONG / SHORT | ⏳ Pendiente |
| O005 | Fortalecer la robustez | ⏳ Pendiente |
| O006 | Validar estrategias alternativas | ⏳ Pendiente |
| O007 | Optimizar parámetros | ⏳ Pendiente |
| O008 | Ampliar mercados | ⏳ Pendiente |
| O009 | Reserva estratégica | Disponible |

---

## 7.5 Prioridades Estratégicas (P)

Las Prioridades establecen el orden recomendado para la evolución de la estrategia.

| Código | Dominio | Estado |
|----------|----------|---------|
| P001 | Completar evidencia estadística | ⏳ Pendiente |
| P002 | Recuperar ventaja estadística | ⏳ Pendiente |
| P003 | Reducir Drawdown | ⏳ Pendiente |
| P004 | Incrementar consistencia | ⏳ Pendiente |
| P005 | Optimizar activos | ⏳ Pendiente |
| P006 | Optimizar LONG / SHORT | ⏳ Pendiente |
| P007 | Comparar versiones | ⏳ Pendiente |
| P008 | Consolidar nueva estrategia | ⏳ Pendiente |
| P009 | Reserva estratégica | Disponible |

---

## 7.6 Conclusión Estratégica (C)

La Conclusión General constituye la síntesis final del conocimiento generado por el Analizador.

No representa una nueva regla, sino la integración de toda la información producida por las categorías anteriores.

| Código | Dominio | Estado |
|----------|----------|---------|
| C001 | Conclusión Estratégica Global | ⏳ Pendiente |

---

# 8. Plantilla Oficial de una Regla

Toda regla deberá documentarse utilizando la siguiente estructura.

- Código.
- Nombre.
- Dominio.
- Prioridad.
- Evidencias utilizadas.
- Condiciones de activación.
- Interpretación.
- Salida esperada.
- Estado de implementación.
- Versión del Analizador.

---

# 9. Estado de Implementación

| Grupo | Implementadas | Total |
|---------|---------------|-------|
| Fortalezas | 1 | 9 |
| Debilidades | 0 | 9 |
| Riesgos | 0 | 9 |
| Oportunidades | 0 | 9 |
| Prioridades | 0 | 9 |
| Conclusión | 0 | 1 |

Total implementadas: **1 de 46 reglas**.

---

# 10. Historial de Cambios

## Versión 1.0

- Creación del Catálogo Oficial del Motor de Hallazgos Estratégicos.
- Definición de la Base de Conocimiento del Analizador.
- Incorporación de la estructura metodológica oficial.
- Incorporación del catálogo de dominios estratégicos.
- Registro de la primera regla implementada (F001).

## Versión 1.1.

- Implementación oficial F002;
- Incorporación de configuración centralizada;
- Separación entre configuración y lógica;
- Consolidación del patrón arquitectónico para futuras reglas.

# 11. Ciclo de Vida de una Regla

Toda regla seguirá el siguiente proceso.

Propuesta

↓

Documentación

↓

Implementación

↓

Validación estadística

↓

Liberación

↓

Mantenimiento

Una regla nunca deberá incorporarse al Analizador sin haber sido previamente documentada en este catálogo.

# 12. Buenas Prácticas para Implementar Reglas

- Cada regla es completamente independiente;
- Ninguna regla llama otra regla;
- Ninguna regla recalcula métricas;
- Todas reciben las mismas entradas (metricas, diagnostico, evidencia);
- Toda configuración proviene de REGLAS_HALLAZGOS;
- Una regla únicamente devuelve None o el texto del hallazgo;
- Una regla nunca modifica datos de entrada.