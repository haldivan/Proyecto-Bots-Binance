# PROYECTO_BOTS_BINANCE.md

Versión: 2.2
Última actualización: Julio 2026
---

# 0. Estado del Proyecto

## Estado General

| Componente | Estado Actual |
|------------|---------------|
| Bot Crypto | ✅ Producción (Dinero Real) |
| Bot TradFi | ✅ Validación Estadística (Modo Observación) |
| Analizador de Estadísticas | ✅ Versión 1.0 (Arquitectura Consolidada) |
| Sistema de Estadísticas | ✅ Consolidado |
| Infraestructura | 🟡 Desarrollo Local |
| Fase del Proyecto | Validación Estadística |

---

## Versiones Oficiales

### Bot Crypto

Versión actual:

```text
Fase1.1_MACD_BTC1H
```

Estado:

- Producción con dinero real.
- Estrategia Fase 1 congelada.
- Score NORMALIZADO_V1 implementado.
- Histórico completo preservado para futuras comparaciones.

---

### Bot TradFi

Versión actual:

```text
Fase1.2_MACD_QQQ1H
```

Estado:

- Modo Observación.
- Evaluación automática de operaciones.
- Score NORMALIZADO_V1 implementado.
- Validación estadística previa a la transición hacia dinero real.
- Histórico completo preservado.

---

### Analizador de Estadísticas

Versión actual:

```text
Versión 1.0
```

Estado:

Arquitectura funcional consolidada.

Módulos implementados:

- Validación de consistencia.
- Resumen general.
- LONG vs SHORT.
- Estadísticas por símbolo.
- Métricas financieras.
- Profit Factor.
- Reward / Risk.
- Expectancy.
- Recovery Factor.
- Curva de Capital.
- Maximum Drawdown.
- Rachas.
- Diagnóstico Automático.
- Score Estratégico.
- Motor de Evidencia.

El siguiente desarrollo corresponde al módulo de Hallazgos Estratégicos, encargado de transformar las métricas y el diagnóstico en conclusiones automáticas sin recalcular indicadores.

---

## Objetivo de la fase actual

El proyecto continúa en la etapa de Validación Estadística.

El objetivo principal no consiste en maximizar la rentabilidad inmediata, sino obtener evidencia cuantitativa suficiente para determinar si las estrategias implementadas poseen una ventaja estadística sostenible.

Durante esta fase:

- Las reglas principales de trading permanecen congeladas.
- Las modificaciones permitidas se limitan a estabilidad, arquitectura, mantenibilidad y calidad del software.
- Toda optimización futura deberá sustentarse en evidencia estadística generada por el Analizador.

La transición hacia nuevas versiones de estrategia únicamente se realizará cuando los resultados estadísticos justifiquen objetivamente dicho cambio.

---

## Principios vigentes de la fase

Durante la fase actual se consideran consolidadas las siguientes decisiones:

- Mantener la comparabilidad entre versiones de estrategia.
- Preservar íntegramente el histórico de operaciones.
- Identificar explícitamente la versión del bot y el modelo de Score utilizado en cada operación.
- Evitar modificaciones que invaliden la evidencia estadística acumulada.
- Priorizar arquitectura, estabilidad y calidad del software sobre la incorporación de nuevas funcionalidades.

## Estado del Analizador.

- Analizador pasa de "Hallazgos Estratégicos en desarrollo" a "Motor de Hallazgos parcialmente implementado".
- Agregar que existe un catálogo metodológico independiente.
- Registrar que F001 y F002 ya están implementadas.
- El siguiente objetivo pasa a ser F003–F008.

# 1. Objetivo General

El Proyecto Bots Binance tiene como objetivo desarrollar una plataforma modular de investigación, validación y ejecución de estrategias cuantitativas sobre Binance, diseñada bajo principios de arquitectura escalable, separación de responsabilidades y toma de decisiones basada en evidencia estadística.

La plataforma integra componentes especializados que cubren todo el ciclo de vida de una estrategia de trading:

1. Diseño e implementación de estrategias.
2. Ejecución en mercados reales o en modo observación.
3. Registro estructurado de todas las operaciones.
4. Análisis estadístico independiente.
5. Interpretación automática de resultados.
6. Optimización controlada basada en evidencia.
7. Comparación objetiva entre versiones de estrategia.

El propósito del proyecto no consiste únicamente en construir bots rentables, sino en establecer un proceso reproducible de investigación cuantitativa que permita evolucionar las estrategias de forma ordenada, medible y estadísticamente sustentada.

---

## Alcance del Proyecto

Actualmente la plataforma está compuesta por los siguientes módulos principales:

### Bot Crypto

Sistema de ejecución automática para criptomonedas sobre Binance Futures.

Opera con dinero real y constituye el entorno de producción del proyecto.

---

### Bot TradFi

Sistema de validación para activos tradicionales tokenizados disponibles en Binance.

Opera en Modo Observación y permite validar estrategias antes de su transición hacia producción.

---

### Sistema de Estadísticas

Repositorio oficial de todas las operaciones generadas por los bots.

Constituye la única fuente de información utilizada para los análisis posteriores.

---

### Analizador de Estadísticas

Motor independiente encargado de transformar los datos históricos en métricas objetivas, diagnósticos y evidencia cuantitativa para apoyar la evolución de las estrategias.

---

## Visión de Largo Plazo

La arquitectura fue concebida para incorporar progresivamente nuevos componentes sin alterar los ya existentes.

Entre las capacidades previstas se encuentran:

- Comparación automática entre versiones de estrategia.
- Backtesting reutilizable.
- Reportes automáticos.
- Dashboard estadístico.
- Automatización del proceso de investigación.
- Nuevos bots especializados.
- Herramientas de apoyo mediante Inteligencia Artificial.

Cada nueva capacidad deberá integrarse respetando la arquitectura modular y la metodología de validación estadística definidas en este documento.

---

## Objetivo Estratégico

El objetivo final del proyecto es disponer de una plataforma capaz de responder, mediante evidencia cuantitativa, preguntas como:

- ¿La estrategia posee ventaja estadística?
- ¿Qué versión obtiene mejores resultados?
- ¿Qué modificaciones realmente mejoran el desempeño?
- ¿Qué componentes explican las ganancias o las pérdidas?
- ¿Cuándo existe suficiente evidencia para evolucionar una estrategia?

Todas las decisiones de desarrollo deberán orientarse a responder estas preguntas de forma objetiva, reproducible y sustentada en datos históricos.

# 2. Filosofía del Proyecto

Todo el desarrollo del Proyecto Bots Binance se fundamenta en una filosofía de investigación cuantitativa, donde cada decisión técnica debe ser objetiva, reproducible y respaldada por evidencia estadística.

La prioridad del proyecto no es desarrollar rápidamente nuevas funcionalidades, sino construir una plataforma robusta cuya evolución pueda medirse y justificarse mediante datos.

---

## 2.1 Desarrollo incremental

Las estrategias evolucionan mediante fases claramente definidas.

Cada nueva versión deberá introducir un conjunto reducido de cambios para que su impacto pueda evaluarse de forma independiente.

No se realizarán modificaciones simultáneas que impidan identificar el efecto real de cada cambio sobre el desempeño de la estrategia.

La evolución del sistema deberá ser completamente trazable.

---

## 2.2 Decisiones basadas en evidencia

Las decisiones de optimización no se fundamentarán en percepciones, intuiciones ni resultados aislados.

Toda modificación permanente deberá estar respaldada por evidencia obtenida mediante el Analizador de Estadísticas.

La evidencia tendrá siempre prioridad sobre la opinión.

---

## 2.3 Separación de responsabilidades

Cada componente del proyecto posee una única responsabilidad claramente definida.

- Los bots analizan el mercado y ejecutan operaciones.
- El Sistema de Estadísticas registra el historial de operaciones.
- El Analizador transforma los datos en información cuantitativa.
- Los reportes presentan los resultados.
- La metodología define cuándo una estrategia puede evolucionar.

Ningún componente deberá asumir funciones que correspondan a otro.

Esta separación constituye uno de los pilares de la arquitectura del proyecto.

---

## 2.4 Validación antes que optimización

Durante la fase de validación estadística las reglas principales de la estrategia permanecerán congeladas.

Mientras no exista una muestra representativa únicamente se permitirán modificaciones destinadas a:

- corregir errores;
- mejorar estabilidad;
- optimizar la arquitectura;
- reducir consumo de recursos;
- incrementar la mantenibilidad del software.

Las reglas de trading únicamente podrán modificarse cuando exista evidencia suficiente que justifique objetivamente dicho cambio.

---

## 2.5 Comparabilidad histórica

Toda evolución deberá preservar la posibilidad de comparar objetivamente distintas versiones de una estrategia.

Para ello:

- se conservarán los registros históricos;
- cada operación identificará explícitamente la versión del bot;
- cada operación identificará el modelo de Score utilizado;
- las nuevas versiones nunca deberán invalidar la evidencia acumulada por versiones anteriores.

La comparabilidad constituye un requisito obligatorio para la evolución del proyecto.

---

## 2.6 Arquitectura modular

Todos los componentes deberán desarrollarse como módulos independientes y reutilizables.

La incorporación de nuevas herramientas no deberá requerir modificaciones significativas en los componentes existentes.

Esta filosofía permitirá incorporar futuras capacidades como:

- comparación automática entre estrategias;
- backtesting;
- dashboards;
- reportes automáticos;
- nuevos bots especializados.

---

## 2.7 Reproducibilidad

Un mismo conjunto de datos deberá producir siempre exactamente los mismos resultados.

Los procesos de análisis no dependerán del momento de ejecución ni del estado del mercado.

Esto garantiza que cualquier resultado pueda verificarse posteriormente.

---

## 2.8 Investigación cuantitativa

El proyecto adopta un enfoque de investigación continua.

Cada estrategia seguirá un ciclo permanente:

1. Diseñar.
2. Implementar.
3. Validar.
4. Medir.
5. Analizar.
6. Optimizar.
7. Comparar.
8. Repetir.

Cada iteración deberá generar conocimiento que permita mejorar la siguiente versión de la estrategia.

---

## 2.9 Evolución basada en conocimiento

El objetivo del proyecto no consiste únicamente en generar métricas.

El propósito final es transformar los datos históricos en conocimiento útil para comprender:

- por qué una estrategia funciona;
- por qué deja de funcionar;
- qué modificaciones producen mejoras reales;
- qué cambios deben descartarse.

La evolución del proyecto estará guiada por el conocimiento obtenido a partir de la evidencia estadística y no únicamente por los resultados financieros obtenidos.

# 3. Principios Técnicos Consolidados

Las decisiones descritas en este capítulo constituyen la arquitectura oficial del proyecto.

Se consideran principios permanentes y no deberán modificarse salvo que exista evidencia estadística o una justificación técnica suficientemente sólida.

Su objetivo es preservar la estabilidad, la comparabilidad histórica y la coherencia de la plataforma durante su evolución.

---

# 3.1 Separación entre Ejecución y Análisis

Los bots tienen como única responsabilidad analizar el mercado y ejecutar operaciones.

El análisis estadístico se realiza exclusivamente mediante herramientas independientes.

Esta separación garantiza que:

- los bots no modifiquen su comportamiento en función de resultados recientes;
- el análisis pueda repetirse sobre los mismos datos;
- la evolución de las estrategias permanezca controlada.

En consecuencia:

- los bots nunca consultarán métricas históricas para decidir una operación;
- el Analizador nunca enviará órdenes a Binance;
- los archivos históricos constituyen el único vínculo entre ambos componentes.

---

# 3.2 Congelamiento de Estrategias

Durante la fase de validación estadística las reglas operativas permanecerán congeladas.

Se consideran reglas de estrategia:

- indicadores utilizados;
- filtros maestros;
- reglas de entrada;
- reglas de salida;
- parámetros de gestión del riesgo.

Únicamente podrán modificarse cuando exista evidencia estadística suficiente para justificar una nueva versión.

---

# 3.3 Comparabilidad entre Versiones

Toda evolución deberá permitir comparar objetivamente las distintas versiones de una estrategia.

Para ello:

- cada operación registrará la versión del bot utilizada;
- cada operación registrará el modelo de Score correspondiente;
- las estadísticas históricas nunca serán eliminadas;
- los cambios arquitectónicos deberán preservar la compatibilidad con los análisis anteriores.

La comparación entre versiones constituye uno de los objetivos centrales del proyecto.

---

# 3.4 Modelo de Score

El Score representa un mecanismo de priorización entre múltiples oportunidades válidas detectadas durante un mismo ciclo de análisis.

El algoritmo de Score forma parte de la estrategia y, por tanto, constituye un elemento versionable.

Cada operación deberá identificar explícitamente el modelo de Score utilizado, permitiendo comparar objetivamente distintos algoritmos en el futuro.

La evolución del Score nunca deberá comprometer la comparabilidad de las estadísticas históricas.

---

# 3.5 Registro Histórico Inmutable

El historial de operaciones constituye la fuente oficial de información del proyecto.

Como principio general:

- las operaciones cerradas no deberán modificarse;
- las nuevas versiones nunca sustituirán registros anteriores;
- toda información adicional se incorporará mediante nuevos campos, evitando alterar el significado de los ya existentes.

Este principio garantiza la trazabilidad completa del proceso de investigación.

---

# 3.6 Arquitectura Modular

Cada componente deberá mantener una única responsabilidad.

La incorporación de nuevas funcionalidades deberá realizarse mediante módulos independientes, evitando introducir dependencias innecesarias entre los distintos componentes.

La modularidad constituye un requisito indispensable para la futura incorporación de:

- nuevos bots;
- Backtesting;
- comparador de estrategias;
- dashboards;
- reportes automáticos;
- herramientas de Inteligencia Artificial.

---

# 3.7 Compatibilidad Evolutiva

Toda mejora deberá diseñarse de forma que preserve la compatibilidad con las versiones anteriores.

Cuando una nueva funcionalidad requiera información adicional:

- se añadirán nuevos campos antes de modificar los existentes;
- se documentará claramente el cambio;
- el Analizador deberá continuar interpretando correctamente los históricos anteriores siempre que sea técnicamente posible.

La compatibilidad constituye un requisito arquitectónico permanente.

---

# 3.8 Evidencia como Criterio de Decisión

Las decisiones técnicas relacionadas con la evolución de las estrategias deberán fundamentarse en evidencia cuantitativa.

Como criterio general:

- una operación individual no constituye evidencia;
- una racha aislada no constituye evidencia;
- una mejora deberá demostrarse mediante muestras representativas y métricas objetivas.

Este principio tiene prioridad sobre cualquier percepción subjetiva derivada del comportamiento reciente del mercado.

---

# 3.9 Prioridades de Desarrollo

El orden oficial de prioridades del proyecto será siempre:

1. Correctitud funcional.
2. Estabilidad.
3. Calidad arquitectónica.
4. Integridad de los datos.
5. Evidencia estadística.
6. Rendimiento.
7. Incorporación de nuevas funcionalidades.

Ninguna nueva característica justificará comprometer la estabilidad o la calidad de la arquitectura existente.

# 4. Arquitectura General del Proyecto

## 4.1 Visión General

El Proyecto Bots Binance está construido sobre una arquitectura modular organizada por capas funcionales.

Cada capa posee una única responsabilidad y se comunica con las demás únicamente mediante interfaces claramente definidas.

Esta organización reduce el acoplamiento entre componentes, facilita el mantenimiento y permite incorporar nuevas funcionalidades sin afectar el funcionamiento del sistema existente.

La arquitectura actual se representa de la siguiente manera:

```text
                    ┌──────────────────────┐
                    │     Binance API      │
                    └──────────┬───────────┘
                               │
               ┌───────────────┴───────────────┐
               │                               │
       ┌───────▼────────┐             ┌────────▼───────┐
       │   Bot Crypto    │             │   Bot TradFi   │
       └───────┬────────┘             └────────┬───────┘
               │                               │
               └───────────────┬───────────────┘
                               │
                     Sistema de Estadísticas
                               │
                               ▼
                 datos/ (CSV oficiales)
                               │
                               ▼
                Analizador de Estadísticas
                               │
                               ▼
              Diagnóstico • Evidencia • Hallazgos
                               │
                               ▼
                     Decisiones de Optimización
```

Cada bloque puede evolucionar de forma independiente mientras mantenga su interfaz con el resto del sistema.

---

# 4.2 Capas Arquitectónicas

La plataforma se divide en cinco capas principales.

## Capa de Ejecución

Responsable de interactuar con Binance.

Está formada por:

- Bot Crypto.
- Bot TradFi.

Sus responsabilidades son:

- obtener información del mercado;
- calcular indicadores;
- detectar oportunidades;
- ejecutar o simular operaciones;
- registrar todas las operaciones.

Los bots no realizan análisis estadísticos ni toman decisiones de optimización.

---

## Capa de Persistencia

Está compuesta por los archivos almacenados en el directorio:

```text
datos/
```

Constituye la fuente oficial de información histórica del proyecto.

Todos los componentes posteriores trabajan exclusivamente sobre estos archivos.

La persistencia desacopla completamente la ejecución del análisis.

---

## Capa Analítica

Representada por:

```text
herramientas/
analizar_estadisticas.py
```

Su función consiste en transformar datos históricos en métricas objetivas.

Esta capa nunca modifica archivos de estadísticas ni interactúa con Binance.

---

## Capa de Inteligencia

Construida sobre el Analizador.

Integra:

- métricas;
- diagnóstico automático;
- motor de evidencia;
- hallazgos estratégicos (fase actual);
- futuras comparaciones entre versiones.

Esta capa transforma información cuantitativa en conocimiento útil para la evolución de las estrategias.

---

## Capa de Decisión

Corresponde al proceso metodológico mediante el cual se determina si una estrategia debe mantenerse o evolucionar.

Las decisiones nunca se toman directamente desde los bots.

Siempre se fundamentan en los resultados obtenidos por el Analizador de Estadísticas.

---

# 4.3 Flujo Oficial de Información

El flujo oficial del proyecto es el siguiente:

```text
Mercado

↓

Bots

↓

Sistema de Estadísticas

↓

Analizador

↓

Diagnóstico

↓

Motor de Evidencia

↓

Hallazgos Estratégicos

↓

Optimización de Estrategias
```

Cada etapa consume exclusivamente la información generada por la etapa anterior.

No existen dependencias inversas.

---

# 4.4 Componentes del Proyecto

Actualmente la plataforma está formada por los siguientes componentes principales.

## Bot Crypto

Sistema de ejecución automática para criptomonedas.

Opera con dinero real.

Su función es generar operaciones reales y registrar completamente cada ejecución.

---

## Bot TradFi

Sistema de validación para activos tradicionales tokenizados.

Opera en Modo Observación.

Permite validar nuevas estrategias antes de incorporarlas al entorno de producción.

---

## Sistema de Estadísticas

Repositorio histórico del proyecto.

Registra todas las operaciones y constituye la única fuente oficial utilizada para el análisis cuantitativo.

---

## Analizador de Estadísticas

Herramienta independiente encargada de:

- validar datos;
- calcular métricas;
- generar diagnósticos;
- producir evidencia objetiva;
- asistir el proceso de investigación.

Representa el núcleo analítico del proyecto.

---

# 4.5 Principios Arquitectónicos

La arquitectura del proyecto se rige por los siguientes principios.

## Bajo acoplamiento

Cada componente puede evolucionar sin modificar los demás.

---

## Alta cohesión

Cada módulo posee una única responsabilidad claramente definida.

---

## Escalabilidad

La incorporación de nuevos bots o herramientas no deberá requerir cambios significativos en la arquitectura existente.

---

## Compatibilidad

Las nuevas versiones deberán preservar la posibilidad de analizar información histórica previamente generada.

---

## Reutilización

Los componentes deberán diseñarse para ser reutilizados por futuras herramientas, como:

- Backtesting;
- Comparador de Estrategias;
- Dashboards;
- Reportes automáticos;
- Inteligencia Artificial.

---

# 4.6 Evolución Arquitectónica

La arquitectura actual constituye la base sobre la cual evolucionará toda la plataforma.

Las siguientes capacidades se integrarán reutilizando los componentes existentes:

- Comparación automática entre versiones.
- Análisis temporal.
- Backtesting.
- Reportes automáticos.
- Dashboards estadísticos.
- Nuevos bots especializados.

La incorporación de estas funcionalidades no deberá alterar las responsabilidades actuales de cada componente.

# 5. Bot Crypto

## 5.1 Objetivo

El Bot Crypto constituye el entorno de producción del proyecto.

Su responsabilidad es detectar oportunidades de inversión en el mercado de criptomonedas, ejecutar operaciones reales sobre Binance Futures y registrar toda la información necesaria para su posterior análisis estadístico.

Durante la Fase 1 el objetivo principal no consiste en maximizar la rentabilidad inmediata, sino validar estadísticamente la estrategia mediante operaciones reales y construir una base de evidencia suficientemente representativa para futuras optimizaciones.

---

# 5.2 Estado Actual

Versión oficial:

```text
Fase1.1_MACD_BTC1H
```

Estado:

- Producción con dinero real.
- Estrategura Fase 1 congelada.
- Modelo de Score NORMALIZADO_V1 implementado.
- Compatible con el Analizador de Estadísticas v1.0.
- Histórico completo preservado para futuras comparaciones.

---

# 5.3 Universo de Activos

Actualmente el bot analiza los siguientes instrumentos:

- SOLUSDT
- XRPUSDT
- ADAUSDT
- DOTUSDT
- TRXUSDT
- NEARUSDT
- UNIUSDT
- AVAXUSDT
- BNBUSDT

La incorporación o eliminación de activos únicamente podrá realizarse cuando exista evidencia estadística suficiente para justificar dicho cambio.

---

# 5.4 Parámetros Operativos

Los parámetros oficiales de la estrategia son:

| Parámetro | Valor |
|-----------|------:|
| Mercado | Binance Futures |
| Temporalidad | 15 minutos |
| Apalancamiento | 3x |
| Margen | Aislado |
| Capital fijo por operación | 2.5 USDT |
| Máximo de posiciones simultáneas | 3 |

Estos parámetros permanecerán congelados durante la fase de validación estadística.

---

# 5.5 Arquitectura Funcional

El funcionamiento del Bot Crypto se organiza en los siguientes módulos:

## Sincronización

Coordina la ejecución del bot con el cierre de las velas de trabajo.

Esto garantiza que todas las decisiones se tomen utilizando información consistente y evita operar sobre velas aún no confirmadas.

---

## Contexto de Mercado

Antes de analizar cualquier activo, el bot determina la dirección general del mercado mediante el Filtro Maestro BTC.

Este contexto se calcula una única vez por ciclo y posteriormente se reutiliza para todos los activos analizados.

---

## Análisis Individual

Cada activo se procesa de forma independiente.

Durante esta etapa se calculan:

- EMA 20
- SMA 50
- RSI (14)
- MACD
- Línea Signal

Posteriormente se evalúan las reglas de entrada LONG o SHORT.

---

## Ranking de Oportunidades

Todas las oportunidades válidas detectadas durante un ciclo son almacenadas temporalmente.

Posteriormente se ordenan mediante el modelo de Score vigente.

Únicamente las mejores oportunidades son seleccionadas hasta completar el límite máximo de posiciones permitido.

---

## Ejecución

Las oportunidades seleccionadas generan órdenes reales sobre Binance Futures.

Cada operación incorpora automáticamente:

- versión de estrategia;
- modelo de Score;
- información del contexto de mercado;
- parámetros operativos necesarios para su posterior análisis.

---

## Registro Estadístico

Toda operación ejecutada queda registrada automáticamente en el Sistema de Estadísticas.

El registro constituye la fuente oficial utilizada posteriormente por el Analizador.

---

# 5.6 Filtro Maestro BTC

El Filtro Maestro BTC representa el contexto general del mercado.

Actualmente utiliza:

- BTCUSDT
- Temporalidad de 1 hora
- EMA 20
- EMA 50

Condición alcista:

```text
EMA20 > EMA50
```

Condición bajista:

```text
EMA20 < EMA50
```

El resultado se calcula una única vez por ciclo para garantizar coherencia entre todas las oportunidades evaluadas.

---

# 5.7 Estrategia Operativa

La estrategia actual combina tres componentes principales:

## Tendencia

Confirmada mediante la relación entre EMA20 y SMA50.

---

## Momentum

Confirmado mediante MACD y su línea Signal.

---

## Fortaleza Relativa

Evaluada mediante RSI dentro de rangos predefinidos.

La operación únicamente se ejecuta cuando las tres condiciones son compatibles con el contexto general definido por el Filtro Maestro BTC.

---

# 5.8 Modelo de Score

La versión actual utiliza el modelo:

```text
NORMALIZADO_V1
```

Este modelo elimina el sesgo producido por el precio nominal de los activos mediante la normalización independiente de sus componentes.

El algoritmo de Score forma parte de la estrategia y se considera un elemento versionable.

Cada operación registra explícitamente el modelo utilizado para preservar la comparabilidad entre versiones futuras.

---

# 5.9 Gestión del Riesgo

La gestión del riesgo implementa:

- capital fijo por operación;
- límite máximo de posiciones abiertas;
- margen aislado;
- apalancamiento controlado;
- Take Profit fijo;
- Stop Loss fijo.

Estos parámetros permanecerán congelados mientras continúe la validación estadística de la Fase 1.

---

# 5.10 Sistema de Estadísticas

El Bot Crypto registra automáticamente toda la información relacionada con la apertura de las operaciones.

Posteriormente el archivo enriquecido incorpora manualmente la información de cierre, permitiendo calcular:

- PnL;
- ROI;
- duración de la operación;
- demás métricas utilizadas por el Analizador.

El archivo enriquecido constituye la fuente oficial para todos los análisis estadísticos del Bot Crypto.

---

# 5.11 Estado de Evolución

La estrategia actual se considera estable.

Durante la fase vigente únicamente se aceptarán modificaciones relacionadas con:

- estabilidad;
- arquitectura;
- mantenibilidad;
- optimización del código;
- calidad del software.

Las reglas operativas permanecerán congeladas hasta completar una muestra estadística suficientemente representativa que justifique objetivamente una nueva versión de la estrategia.

# 6. Bot TradFi

## 6.1 Objetivo

El Bot TradFi constituye el entorno oficial de validación de estrategias del proyecto.

Su propósito es evaluar nuevas versiones de la estrategia sobre activos tradicionales tokenizados disponibles en Binance antes de su incorporación al entorno de producción.

A diferencia del Bot Crypto, su función principal no consiste en generar beneficios económicos inmediatos, sino producir evidencia estadística que permita determinar si una estrategia posee el nivel de madurez suficiente para operar con dinero real.

El Bot TradFi representa el laboratorio experimental del proyecto.

---

# 6.2 Estado Actual

Versión oficial:

```text
Fase1.2_MACD_QQQ1H
```

Estado actual:

- Modo Observación.
- Evaluación automática de operaciones.
- Modelo de Score NORMALIZADO_V1.
- Compatible con el Analizador de Estadísticas v1.0.
- Histórico completo preservado para futuras comparaciones.

Su misión actual consiste en completar la validación estadística de la estrategia antes de una eventual transición controlada hacia producción.

---

# 6.3 Universo de Activos

Actualmente el bot analiza los siguientes instrumentos:

- NVDAUSDT
- AMDUSDT
- MSFTUSDT
- AAPLUSDT

La incorporación de nuevos activos dependerá exclusivamente de la evidencia estadística obtenida durante la fase de validación.

---

# 6.4 Parámetros Operativos

Los parámetros oficiales de la estrategia son:

| Parámetro | Valor |
|-----------|------:|
| Mercado | Binance Futures |
| Temporalidad | 1 hora |
| Apalancamiento | 1x |
| Margen | Aislado |
| Capital fijo por operación | 5 USDT |
| Máximo de posiciones simultáneas | 2 |

Estos parámetros permanecerán congelados durante la Fase 1.

---

# 6.5 Arquitectura Funcional

El funcionamiento del Bot TradFi se organiza en los siguientes módulos.

## Sincronización

La ejecución se sincroniza con el cierre de cada vela de una hora.

Esto garantiza que todas las decisiones se tomen sobre información confirmada.

---

## Contexto General

Antes de analizar cualquier activo se calcula el contexto general mediante el Filtro Maestro QQQ.

Este cálculo se realiza una única vez por ciclo y posteriormente se reutiliza durante el análisis de todos los instrumentos.

---

## Análisis Individual

Cada activo se analiza de forma independiente.

Durante esta etapa se calculan:

- EMA 20
- SMA 50
- RSI (14)
- MACD
- Línea Signal

Posteriormente se evalúan las reglas de entrada LONG o SHORT.

---

## Ranking de Oportunidades

Todas las señales válidas detectadas durante un ciclo son almacenadas temporalmente.

Posteriormente se ordenan mediante el modelo de Score vigente.

Únicamente las mejores oportunidades son seleccionadas hasta completar el límite máximo de posiciones permitido.

---

## Registro Estadístico

Las oportunidades seleccionadas se registran automáticamente en el Sistema de Estadísticas.

Cada registro incorpora la información necesaria para reconstruir posteriormente el contexto completo de la operación.

---

## Motor de Observación

El Bot TradFi incorpora un mecanismo automático encargado de supervisar continuamente las operaciones abiertas.

Este componente determina el resultado final de cada operación mediante el análisis de las velas históricas generadas con posterioridad a su apertura.

Su funcionamiento es completamente independiente del proceso de detección de nuevas oportunidades.

---

# 6.6 Filtro Maestro QQQ

El contexto general del mercado se determina mediante el ETF tokenizado:

```text
QQQUSDT
```

Actualmente se calculan:

- EMA 20
- EMA 50

Condición alcista:

```text
EMA20 > EMA50
```

Condición bajista:

```text
EMA20 < EMA50
```

El resultado se calcula una única vez por ciclo y se utiliza como filtro para todos los activos analizados.

---

# 6.7 Estrategia Operativa

La estrategia actual combina tres componentes principales.

## Tendencia

Evaluada mediante la relación entre EMA20 y SMA50.

---

## Momentum

Confirmado mediante MACD y su línea Signal.

---

## Fortaleza Relativa

Evaluada mediante RSI dentro de rangos previamente definidos.

La operación únicamente será considerada válida cuando estos tres componentes sean compatibles con el contexto general establecido por el Filtro Maestro QQQ.

---

# 6.8 Modelo de Score

La versión actual implementa el modelo:

```text
NORMALIZADO_V1
```

Este modelo elimina el sesgo provocado por el precio nominal de los distintos activos mediante un proceso de normalización independiente de cada componente.

El modelo de Score forma parte de la estrategia y constituye un elemento versionable.

Cada operación registra explícitamente el modelo utilizado para preservar la comparabilidad entre futuras versiones.

---

# 6.9 Evaluación Automática de Operaciones

El Bot TradFi determina automáticamente el resultado de todas las operaciones registradas.

El proceso de evaluación se basa en los siguientes principios:

- únicamente se revisan operaciones abiertas;
- el análisis continúa desde la última vela procesada;
- cada vela histórica es evaluada una única vez;
- el proceso mantiene su continuidad incluso si el bot se reinicia.

Cuando una operación alcanza su Take Profit o Stop Loss, el sistema actualiza automáticamente toda la información asociada a dicha operación.

Este mecanismo garantiza la consistencia del histórico sin intervención manual.

---

# 6.10 Sistema de Estadísticas

Cada operación registrada incorpora, entre otros, los siguientes elementos:

- versión de la estrategia;
- modelo de Score;
- modo de ejecución;
- Score obtenido;
- contexto del Filtro Maestro QQQ;
- estado de la operación;
- resultado final;
- información de cierre;
- trazabilidad del proceso de evaluación.

Esta información constituye la base utilizada posteriormente por el Analizador de Estadísticas.

---

# 6.11 Heartbeat

El Bot TradFi mantiene un mecanismo de supervisión mediante un archivo Heartbeat.

Su objetivo consiste en facilitar futuros sistemas automáticos de monitoreo capaces de detectar bloqueos, verificar la continuidad del proceso y ejecutar acciones de recuperación cuando resulte necesario.

Actualmente este mecanismo cumple funciones exclusivamente de supervisión.

---

# 6.12 Estado de Evolución

La estrategia actual se considera estable desde el punto de vista arquitectónico.

Durante la fase vigente únicamente se aceptarán modificaciones relacionadas con:

- estabilidad;
- arquitectura;
- mantenibilidad;
- optimización del código;
- calidad del software.

Las reglas operativas permanecerán congeladas hasta completar una muestra estadística suficiente que permita evaluar objetivamente la transición hacia operaciones con dinero real.

La transición a producción únicamente se realizará cuando la evidencia estadística obtenida por el Analizador demuestre que la estrategia presenta un desempeño consistente y comparable con los criterios definidos por la Metodología de Validación Estadística.

# 7. Sistema de Estadísticas

## 7.1 Objetivo

El Sistema de Estadísticas constituye el repositorio oficial de evidencia del Proyecto Bots Binance.

Su función consiste en almacenar de forma estructurada, íntegra y trazable toda la información generada durante la ejecución de las estrategias.

Estos registros representan la única fuente oficial utilizada para:

- evaluar el desempeño de las estrategias;
- comparar versiones del sistema;
- validar hipótesis de investigación;
- generar métricas estadísticas;
- producir diagnósticos automáticos;
- construir evidencia objetiva para la toma de decisiones.

Ninguna conclusión del proyecto podrá fundamentarse en información distinta a la contenida en este sistema.

---

# 7.2 Principios de Diseño

El Sistema de Estadísticas fue diseñado siguiendo los siguientes principios.

## Integridad

Toda operación deberá conservarse una vez registrada.

Los registros históricos constituyen evidencia y no deberán eliminarse ni reemplazarse.

---

## Trazabilidad

Cada operación deberá contener la información necesaria para reconstruir posteriormente el contexto en que fue generada.

Esto incluye, entre otros:

- versión de la estrategia;
- modelo de Score;
- parámetros relevantes;
- resultado final.

---

## Comparabilidad

La estructura del sistema deberá permitir comparar distintas versiones de una misma estrategia.

La incorporación de nuevos campos nunca deberá comprometer la interpretación de la información histórica.

---

## Independencia

El Sistema de Estadísticas constituye una capa completamente independiente de los bots y del Analizador.

Los bots únicamente escriben información.

El Analizador únicamente la consulta.

---

# 7.3 Organización del Directorio

Toda la información histórica se almacena en:

```text
datos/
```

Actualmente este directorio contiene, entre otros, los siguientes archivos oficiales:

```text
estadisticas.csv
estadisticas_crypto.csv
estadisticas_tradfi.csv
senales_detectadas.csv
heartbeat.txt
```

En futuras versiones podrán incorporarse nuevos archivos sin modificar la arquitectura general del sistema.

---

# 7.4 Estadísticas del Bot Crypto

El Bot Crypto registra automáticamente la información correspondiente a la apertura de cada operación.

Posteriormente se mantiene un archivo enriquecido que incorpora la información de cierre necesaria para el análisis estadístico.

El archivo enriquecido constituye la fuente oficial utilizada por el Analizador para evaluar el desempeño del Bot Crypto.

Este enfoque permite preservar el registro operativo original y, al mismo tiempo, disponer de la información necesaria para realizar análisis cuantitativos completos.

---

# 7.5 Estadísticas del Bot TradFi

El Bot TradFi genera automáticamente un registro completo para cada operación.

A diferencia del Bot Crypto, tanto la apertura como el cierre de las operaciones son gestionados por el propio sistema.

Cada registro incorpora información suficiente para reconstruir completamente el ciclo de vida de la operación, incluyendo su proceso de evaluación automática.

Este archivo constituye la fuente oficial para todos los análisis relacionados con el Bot TradFi.

---

# 7.6 Información Registrada

Como principio general, cada operación deberá registrar toda la información necesaria para su posterior análisis.

Dependiendo del bot y de la versión de la estrategia, los registros podrán incluir, entre otros:

- fecha y hora de apertura;
- símbolo;
- dirección de la operación;
- precio de entrada;
- Take Profit;
- Stop Loss;
- Score obtenido;
- modelo de Score;
- versión de la estrategia;
- contexto del mercado;
- estado de la operación;
- fecha y hora de cierre;
- precio de cierre;
- resultado;
- PnL;
- ROI;
- información de seguimiento.

La incorporación de nuevos campos deberá realizarse preservando la compatibilidad con los registros históricos.

---

# 7.7 Registro de Señales

El archivo:

```text
senales_detectadas.csv
```

almacena las señales detectadas por el Bot Crypto durante cada ciclo de análisis.

En la arquitectura actual este archivo refleja únicamente las oportunidades que alcanzan la etapa final del proceso de selección.

Debido a la restricción impuesta por el límite de posiciones simultáneas, este registro no representa la totalidad de las oportunidades existentes en el mercado.

Por esta razón, el análisis estadístico de señales queda postergado hasta la Fase 2 del proyecto.

En dicha fase el bot registrará todas las señales detectadas antes de aplicar cualquier criterio de selección, permitiendo evaluar objetivamente el desempeño del algoritmo de priorización.

---

# 7.8 Heartbeat

El archivo:

```text
heartbeat.txt
```

constituye un mecanismo de supervisión del estado operativo de los bots.

Su función es facilitar la futura implementación de herramientas automáticas de monitoreo capaces de detectar interrupciones, verificar la continuidad de la ejecución y activar procedimientos de recuperación.

Actualmente cumple funciones exclusivamente de monitoreo.

---

# 7.9 Flujo Oficial de la Información

El flujo oficial del Sistema de Estadísticas es el siguiente:

```text
Bots

↓

Registro de operaciones

↓

Sistema de Estadísticas

↓

Analizador

↓

Diagnóstico

↓

Motor de Evidencia

↓

Hallazgos Estratégicos

↓

Decisiones de Optimización
```

Los archivos históricos representan el punto de unión entre la ejecución de las estrategias y el proceso de investigación cuantitativa.

---

# 7.10 Integridad del Histórico

La validez de cualquier análisis depende directamente de la integridad de los datos registrados.

Como principio permanente:

- los registros históricos no deberán eliminarse;
- las operaciones cerradas no deberán modificarse;
- las correcciones deberán documentarse;
- las nuevas versiones deberán preservar la evidencia acumulada.

La calidad del Sistema de Estadísticas determina la calidad de todas las conclusiones obtenidas posteriormente.

---

# 7.11 Evolución Futura

El Sistema de Estadísticas continuará ampliándose conforme evolucionen las necesidades del proyecto.

Entre las capacidades previstas se encuentran:

- cálculo automático del PnL para el Bot Crypto;
- almacenamiento de comisiones;
- registro del capital acumulado;
- incorporación de nuevas variables de contexto;
- soporte para múltiples estrategias simultáneas;
- integración con Backtesting;
- integración con el Comparador de Estrategias.

Toda ampliación deberá respetar los principios de integridad, trazabilidad y comparabilidad establecidos en este capítulo.

# 8. Analizador de Estadísticas

## 8.1 Objetivo

El Analizador de Estadísticas constituye el núcleo de inteligencia cuantitativa del Proyecto Bots Binance.

Su propósito consiste en transformar los datos históricos generados por los bots en información objetiva, evidencia estadística y conocimiento útil para la evolución controlada de las estrategias.

El Analizador representa el mecanismo oficial mediante el cual se determina si una estrategia debe mantenerse, modificarse o descartarse.

Ninguna decisión relacionada con la evolución de una estrategia deberá fundamentarse en información distinta a la producida por este módulo.

---

# 8.2 Principios de Diseño

El Analizador fue desarrollado bajo los siguientes principios.

## Independencia

El Analizador nunca interactúa con Binance.

No consulta precios.

No ejecuta operaciones.

No modifica estrategias.

Trabaja exclusivamente sobre archivos históricos.

---

## Reproducibilidad

Un mismo conjunto de datos deberá producir exactamente los mismos resultados.

El análisis nunca dependerá del estado del mercado ni del momento de ejecución.

---

## Modularidad

Cada capacidad del Analizador se implementa como un módulo independiente.

Esto permite incorporar nuevas funcionalidades sin modificar el comportamiento existente.

---

## Compatibilidad

El Analizador deberá mantener compatibilidad con diferentes versiones de estrategias y distintos modelos de Score.

La incorporación de nuevas funcionalidades no deberá invalidar la interpretación de los históricos existentes.

---

# 8.3 Arquitectura General

La arquitectura del Analizador se organiza en capas funcionales.

```text
Carga de Datos

↓

Validación

↓

Normalización

↓

Motor Estadístico

↓

Diagnóstico Automático

↓

Motor de Evidencia

↓

Hallazgos Estratégicos

↓

Presentación de Resultados
```

Cada capa posee una única responsabilidad claramente definida.

Esta arquitectura facilita la evolución del sistema sin afectar los módulos previamente consolidados.

---

# 8.4 Capas Funcionales

## Carga de Datos

Responsable de localizar, cargar y preparar los archivos oficiales de estadísticas.

---

## Validación

Verifica la integridad estructural de la información.

Detecta inconsistencias antes de iniciar cualquier análisis.

---

## Normalización

Adapta las diferencias existentes entre distintos formatos de archivos y versiones de estrategia.

Gracias a esta capa el Analizador puede trabajar sobre múltiples generaciones de datos manteniendo una interfaz común.

---

## Motor Estadístico

Calcula todas las métricas objetivas del proyecto.

Entre ellas:

- Resumen general.
- LONG vs SHORT.
- Estadísticas por símbolo.
- Profit Factor.
- Reward / Risk.
- Expectancy.
- Recovery Factor.
- Curva de Capital.
- Maximum Drawdown.
- Rachas.

---

## Diagnóstico Automático

Interpreta las métricas calculadas y genera una evaluación técnica preliminar del desempeño de la estrategia.

---

## Motor de Evidencia

Integra todas las métricas disponibles para determinar el nivel de evidencia estadística alcanzado por la estrategia.

Este componente constituye la base metodológica para futuras comparaciones entre versiones.

---

## Hallazgos Estratégicos

Transforma el conjunto de métricas, diagnósticos y evidencia en conclusiones automáticas.

Este módulo no recalcula indicadores.

Su función consiste en responder preguntas como:

- ¿Dónde se encuentra la principal debilidad de la estrategia?
- ¿Qué aspecto merece mayor investigación?
- ¿Qué componentes presentan el mejor desempeño?
- ¿Qué cambios deberían priorizarse en futuras versiones?

Representa la transición entre el análisis cuantitativo y la toma de decisiones.

---

# 8.5 Estado Actual

Versión actual:

```text
Analizador de Estadísticas v1.0
```

Estado:

Arquitectura consolidada.

Capacidades implementadas:

- Validación de consistencia.
- Resumen general.
- LONG vs SHORT.
- Estadísticas por símbolo.
- Profit Factor.
- Reward /Risk.
- Expectancy.
- Recovery Factor.
- Curva de Capital.
- Maximum Drawdown.
- Rachas.
- Diagnóstico Automático.
- Score Estratégico.
- Motor de Evidencia.

El siguiente componente a incorporarse corresponde al módulo de Hallazgos Estratégicos.

Una vez implementado este módulo se considerará oficialmente finalizada la versión 1.0 del Analizador.

---

# 8.6 Compatibilidad

El Analizador fue diseñado para operar con:

- distintas versiones de estrategia;
- distintos modelos de Score;
- múltiples archivos históricos;
- información generada por ambos bots.

La compatibilidad constituye uno de los principales objetivos arquitectónicos del sistema.

---

# 8.7 Función dentro del Proyecto

El Analizador constituye la única herramienta autorizada para evaluar objetivamente el desempeño de las estrategias.

En consecuencia:

- los bots no decidirán cuándo optimizarse;
- las optimizaciones no se realizarán por intuición;
- las modificaciones deberán fundamentarse en evidencia estadística.

Este principio forma parte de la metodología oficial del proyecto.

---

# 8.8 Evolución Prevista

La arquitectura actual permitirá incorporar progresivamente nuevas capacidades.

Entre ellas:

- Comparador automático entre versiones.
- Hallazgos Estratégicos.
- Reportes automáticos.
- Exportación de resultados.
- Dashboards estadísticos.
- Análisis temporal.
- Integración con Backtesting.

Estas funcionalidades reutilizarán la arquitectura actualmente consolidada.

---

# 8.9 Filosofía del Analizador

El Analizador no fue diseñado para responder únicamente:

> ¿Cuánto ganó o perdió una estrategia?

Su verdadero propósito consiste en responder preguntas como:

- ¿Existe ventaja estadística?
- ¿Qué explica el desempeño observado?
- ¿Qué componentes limitan la estrategia?
- ¿Qué cambios presentan mayor probabilidad de mejora?
- ¿Qué versión demuestra objetivamente un mejor comportamiento?

En consecuencia, el Analizador constituye el centro de inteligencia cuantitativa del Proyecto Bots Binance.

# 9. Metodología de Validación Estadística

## 9.1 Objetivo

La Metodología de Validación Estadística establece el procedimiento oficial mediante el cual se determina si una estrategia posee evidencia suficiente para evolucionar hacia una nueva versión.

Su finalidad es garantizar que todas las decisiones relacionadas con el desarrollo del proyecto se fundamenten en resultados cuantitativos reproducibles y no en observaciones aisladas del mercado.

Esta metodología constituye el marco científico del Proyecto Bots Binance.

---

# 9.2 Principios Fundamentales

Toda estrategia deberá evaluarse respetando los siguientes principios.

## Evidencia antes que opinión

Las decisiones nunca se basarán en percepciones subjetivas.

Toda modificación deberá estar respaldada por evidencia estadística objetiva.

---

## Reproducibilidad

Los resultados obtenidos deberán poder reproducirse utilizando exactamente el mismo conjunto de datos.

---

## Comparabilidad

Las distintas versiones de una estrategia deberán poder compararse bajo las mismas métricas y criterios de evaluación.

---

## Trazabilidad

Cada conclusión deberá poder relacionarse con los datos históricos que la sustentan.

---

## Evolución incremental

Cada nueva versión deberá introducir un conjunto reducido de cambios para que su impacto pueda medirse objetivamente.

---

# 9.3 Ciclo Oficial de Validación

Toda estrategia seguirá el siguiente ciclo.

```text
Diseño

↓

Implementación

↓

Validación

↓

Obtención de Evidencia

↓

Hallazgos Estratégicos

↓

Optimización

↓

Nueva versión

↓

Comparación

↓

Validación
```

Este ciclo constituye el mecanismo oficial de evolución del proyecto.

---

# 9.4 Tamaño de la Muestra

El proyecto establece tres niveles de confianza.

## Nivel 1

Menos de 50 operaciones cerradas.

Estado:

```text
Muestra insuficiente
```

Durante esta etapa únicamente se aceptarán mejoras relacionadas con:

- estabilidad;
- arquitectura;
- mantenibilidad;
- corrección de errores.

No se modificarán reglas de trading.

---

## Nivel 2

Entre 50 y 70 operaciones cerradas.

Estado:

```text
Muestra mínima para análisis
```

En esta etapa podrán iniciarse análisis completos utilizando el Analizador de Estadísticas.

Las conclusiones deberán interpretarse con prudencia y requerirán confirmación mediante nuevas operaciones.

---

## Nivel 3

Más de 70 operaciones cerradas.

Estado:

```text
Muestra recomendada
```

A partir de este punto podrán evaluarse modificaciones relevantes de la estrategia.

Las decisiones deberán fundamentarse en el comportamiento global de la muestra y no en resultados recientes.

---

# 9.5 Evidencia Estadística

La evidencia estadística constituye el criterio oficial para determinar el grado de confianza alcanzado por una estrategia.

La evidencia se construye mediante la integración de:

- métricas objetivas;
- diagnóstico automático;
- consistencia de resultados;
- comportamiento del riesgo;
- estabilidad del desempeño.

Una estrategia únicamente podrá evolucionar cuando el conjunto de la evidencia justifique objetivamente dicho cambio.

---

# 9.6 Comparación entre Versiones

Toda nueva versión deberá compararse con la versión inmediatamente anterior.

La comparación deberá realizarse utilizando:

- la misma metodología;
- las mismas métricas;
- criterios homogéneos de evaluación;
- muestras estadísticamente comparables.

La adopción de una nueva versión requerirá demostrar una mejora consistente respecto de la versión vigente.

---

# 9.7 Criterios para Evolucionar una Estrategia

Una estrategia podrá evolucionar cuando exista evidencia suficiente de mejora.

Entre los aspectos evaluados se encuentran:

- rentabilidad;
- consistencia;
- estabilidad;
- gestión del riesgo;
- comportamiento por dirección;
- comportamiento por activo;
- desempeño global.

No será suficiente mejorar una única métrica aislada si el desempeño general de la estrategia se deteriora.

---

# 9.8 Prevención de la Sobreoptimización

Uno de los principales riesgos del desarrollo de sistemas de trading es adaptar una estrategia a un conjunto reducido de datos históricos.

Para reducir este riesgo:

- no se optimizarán parámetros continuamente;
- no se modificarán reglas por resultados recientes;
- no se buscará maximizar una única métrica;
- toda modificación deberá demostrar mejoras sostenibles sobre muestras representativas.

La robustez tendrá siempre prioridad sobre la optimización excesiva.

---

# 9.9 Papel del Analizador

El Analizador de Estadísticas constituye la herramienta oficial encargada de aplicar esta metodología.

Su función consiste en transformar los registros históricos en:

- métricas objetivas;
- diagnósticos;
- evidencia;
- hallazgos estratégicos.

Las decisiones de evolución deberán fundamentarse exclusivamente en la información generada por este módulo.

---

# 9.10 Objetivo Final

El propósito de esta metodología no consiste únicamente en desarrollar estrategias rentables.

El objetivo es construir un proceso permanente de investigación cuantitativa capaz de responder, mediante evidencia estadística, qué cambios mejoran realmente una estrategia y cuáles deben descartarse.

De esta manera, la evolución del proyecto se apoyará en conocimiento verificable y no en decisiones intuitivas.


# 10. Roadmap del Proyecto

## 10.1 Visión General

El Proyecto Bots Binance evolucionará de forma incremental siguiendo la metodología de validación estadística definida en este documento.

La evolución no se organiza mediante fases estrictamente secuenciales, sino mediante líneas de desarrollo que podrán avanzar de manera independiente siempre que respeten la arquitectura general del proyecto.

Cada línea representa una capacidad específica de la plataforma y deberá evolucionar sin comprometer la estabilidad de los componentes ya consolidados.

---

# 10.2 Estado Actual

Al momento de esta versión del Documento Maestro, el estado general del proyecto es el siguiente:

| Componente | Estado |
|------------|--------|
| Bot Crypto | ✅ Producción |
| Bot TradFi | ✅ Validación Estadística |
| Sistema de Estadísticas | ✅ Consolidado |
| Analizador de Estadísticas | 🟡 Versión 1.0 (Hallazgos Estratégicos en desarrollo) |
| Comparador de Estrategias | ⏳ No iniciado |
| Backtesting | ⏳ No iniciado |
| Dashboards | ⏳ No iniciado |
| Infraestructura Cloud | ⏳ Pendiente |

La prioridad continúa siendo consolidar la plataforma antes de ampliar su alcance funcional.

---

# 10.3 Línea de Evolución: Bots

Objetivo:

Desarrollar estrategias robustas capaces de operar de manera consistente en distintos contextos de mercado.

Líneas de trabajo:

- evolución controlada de estrategias;
- incorporación de nuevos filtros;
- optimización basada en evidencia;
- validación previa en Bot TradFi;
- despliegue posterior en Bot Crypto.

Toda nueva versión deberá preservar la comparabilidad con las versiones anteriores.

---

# 10.4 Línea de Evolución: Sistema de Estadísticas

Objetivo:

Consolidar un repositorio histórico capaz de soportar todas las necesidades analíticas de la plataforma.

Posibles ampliaciones:

- nuevas variables de contexto;
- comisiones;
- duración de operaciones;
- capital acumulado;
- múltiples estrategias simultáneas;
- nuevos tipos de activos.

---

# 10.5 Línea de Evolución: Analizador

Objetivo:

Convertir el Analizador en el centro de inteligencia cuantitativa del proyecto.

Próximos desarrollos previstos:

- Hallazgos Estratégicos;
- Comparador Automático entre Versiones;
- análisis temporal;
- dashboards;
- exportación de reportes;
- integración con Backtesting.

Toda nueva funcionalidad reutilizará la arquitectura consolidada del Analizador.

---

# 10.6 Línea de Evolución: Investigación Cuantitativa

Objetivo:

Desarrollar herramientas que permitan comprender el comportamiento de las estrategias más allá de sus resultados financieros.

Entre ellas:

- comparación de versiones;
- análisis de estabilidad;
- análisis por condiciones de mercado;
- análisis por Score;
- análisis de señales;
- evaluación de hipótesis.

Estas herramientas complementarán el proceso de investigación sin modificar el funcionamiento de los bots.

---

# 10.7 Línea de Evolución: Backtesting

Objetivo:

Construir un entorno reutilizable para validar nuevas estrategias antes de incorporarlas al proceso operativo.

Capacidades previstas:

- simulación histórica;
- comparación de parámetros;
- análisis de robustez;
- validación cruzada;
- reutilización del Analizador de Estadísticas.

---

# 10.8 Línea de Evolución: Automatización

Objetivo:

Reducir progresivamente la intervención manual durante el proceso de investigación.

Entre las capacidades previstas:

- generación automática de reportes;
- exportación de resultados;
- dashboards interactivos;
- monitoreo de bots;
- alertas automáticas.

---

# 10.9 Línea de Evolución: Infraestructura

Objetivo:

Migrar desde un entorno local hacia una plataforma de ejecución continua.

Líneas de trabajo:

- VPS;
- Oracle Cloud;
- AWS;
- Docker;
- monitoreo remoto;
- reinicio automático;
- respaldo automático.

La evolución de la infraestructura deberá acompañar el crecimiento funcional del proyecto.

---

# 10.10 Línea de Evolución: Inteligencia Artificial

Objetivo:

Incorporar herramientas de IA que complementen el proceso de investigación cuantitativa.

Entre las posibles aplicaciones se encuentran:

- clasificación automática de operaciones;
- detección de patrones;
- agrupamiento de escenarios de mercado;
- asistencia para optimización;
- generación automática de explicaciones.

La Inteligencia Artificial actuará como herramienta de apoyo y nunca reemplazará la metodología de validación estadística.

---

# 10.11 Objetivo Estratégico

La evolución del proyecto persigue un objetivo único:

Construir una plataforma de investigación cuantitativa capaz de desarrollar, validar, comparar y desplegar estrategias de trading de manera completamente trazable, reproducible y basada en evidencia estadística.

Cada nueva capacidad deberá acercar la plataforma a ese objetivo sin comprometer la estabilidad de los componentes previamente consolidados.

# 11. Infraestructura y Despliegue

## 11.1 Objetivo

La infraestructura del Proyecto Bots Binance tiene como finalidad proporcionar un entorno confiable, seguro y escalable para la ejecución continua de todos los componentes de la plataforma.

Su diseño deberá garantizar la continuidad operativa, la integridad de la información y la posibilidad de incorporar nuevos servicios sin modificar la arquitectura existente.

La infraestructura constituye un soporte para la plataforma, no un componente de la estrategia.

---

# 11.2 Estado Actual

Actualmente el proyecto se ejecuta en un entorno local de desarrollo.

Características actuales:

- Visual Studio Code.
- Python 3.x.
- Binance API.
- Variables sensibles gestionadas mediante `.env`.
- Ejecución manual de los procesos.
- Almacenamiento local de estadísticas.
- Desarrollo incremental.

Esta configuración resulta adecuada para la etapa actual de investigación y validación estadística.

---

# 11.3 Principios de Infraestructura

Toda evolución de la infraestructura deberá respetar los siguientes principios.

## Disponibilidad

Los componentes deberán poder ejecutarse de manera continua durante largos períodos de tiempo.

---

## Seguridad

La información sensible deberá permanecer completamente separada del código fuente.

Las credenciales nunca formarán parte del repositorio.

---

## Escalabilidad

La incorporación de nuevos bots o herramientas no deberá requerir rediseñar la infraestructura existente.

---

## Automatización

Las tareas repetitivas deberán automatizarse progresivamente conforme evolucione el proyecto.

---

## Recuperación

La infraestructura deberá permitir detectar fallos y recuperar automáticamente la operación cuando sea posible.

---

# 11.4 Arquitectura de Despliegue

La plataforma evolucionará gradualmente desde un entorno local hacia una infraestructura distribuida.

La evolución prevista comprende:

```text
Desarrollo Local

↓

Servidor VPS

↓

Cloud Computing

↓

Plataforma Distribuida
```

Cada etapa deberá preservar la compatibilidad con la arquitectura previamente consolidada.

---

# 11.5 Monitoreo

La plataforma incorporará mecanismos de supervisión capaces de verificar continuamente el estado operativo de sus componentes.

Entre ellos:

- Heartbeat.
- Logs estructurados.
- Supervisión de procesos.
- Alertas automáticas.
- Reinicio controlado.
- Verificación periódica de ejecución.

Estos mecanismos permitirán minimizar la intervención manual durante la operación.

---

# 11.6 Gestión de Configuración

Toda la configuración deberá mantenerse separada del código fuente.

Entre los elementos configurables se encuentran:

- claves API;
- parámetros de conexión;
- rutas;
- variables de entorno;
- configuraciones específicas de cada entorno.

La separación entre configuración y lógica constituye un principio permanente del proyecto.

---

# 11.7 Gestión de Datos

El Sistema de Estadísticas constituye uno de los activos más importantes del proyecto.

La infraestructura deberá garantizar:

- integridad del histórico;
- respaldo periódico;
- protección frente a pérdidas de información;
- recuperación ante fallos.

La preservación de la evidencia estadística tendrá prioridad sobre cualquier optimización de infraestructura.

---

# 11.8 Evolución Tecnológica

Conforme la plataforma crezca podrán incorporarse nuevas tecnologías.

Entre ellas:

- Docker.
- VPS.
- Oracle Cloud.
- AWS.
- almacenamiento centralizado.
- monitoreo remoto.
- automatización del despliegue.

La adopción de nuevas tecnologías deberá responder a necesidades concretas de la plataforma y no únicamente a criterios tecnológicos.

---

# 11.9 Objetivo de Largo Plazo

La infraestructura evolucionará hasta convertirse en un entorno capaz de ejecutar de forma continua todos los componentes de la plataforma:

- Bots.
- Sistema de Estadísticas.
- Analizador.
- Backtesting.
- Dashboards.
- Herramientas de investigación.

Todo ello manteniendo los principios de estabilidad, seguridad, escalabilidad y mantenibilidad definidos por la arquitectura general del proyecto.

# 12. Decisiones Técnicas Consolidadas

Las decisiones descritas en este capítulo forman parte de la arquitectura oficial del Proyecto Bots Binance.

Se consideran principios permanentes y únicamente podrán modificarse cuando exista una justificación técnica o evidencia estadística suficiente que respalde dicho cambio.

---

# 12.1 Arquitectura

Se consideran decisiones arquitectónicas consolidadas:

- Arquitectura modular basada en separación de responsabilidades.
- Bajo acoplamiento entre componentes.
- Alta cohesión funcional.
- Evolución incremental del software.
- Compatibilidad entre versiones.
- Reutilización de componentes siempre que sea posible.

Toda nueva funcionalidad deberá integrarse respetando estos principios.

---

# 12.2 Bots

Los bots constituyen exclusivamente la capa de ejecución del proyecto.

Como principio permanente:

- los bots analizan el mercado;
- generan señales;
- ejecutan o simulan operaciones;
- registran estadísticas.

Los bots nunca realizarán análisis estadísticos ni decidirán modificaciones sobre la estrategia.

---

# 12.3 Sistema de Estadísticas

El Sistema de Estadísticas constituye el repositorio oficial de evidencia del proyecto.

Como principio permanente:

- las operaciones históricas deberán preservarse;
- toda nueva información se incorporará mediante nuevos campos;
- la información deberá mantenerse trazable y comparable;
- el histórico nunca se reiniciará por cambios de estrategia.

La preservación del histórico constituye un requisito arquitectónico.

---

# 12.4 Analizador de Estadísticas

El Analizador constituye el núcleo de inteligencia cuantitativa del proyecto.

Toda evolución de las estrategias deberá fundamentarse exclusivamente en la información generada por este componente.

El Analizador nunca interactuará directamente con Binance ni modificará archivos de estadísticas.

---

# 12.5 Estrategias

Toda estrategia seguirá el siguiente ciclo oficial:

```text
Diseño

↓

Implementación

↓

Validación

↓

Obtención de Evidencia

↓

Hallazgos Estratégicos

↓

Optimización

↓

Nueva versión

↓

Comparación

↓

Validación
```

La evolución de las estrategias deberá ser completamente trazable.

---

# 12.6 Modelo de Score

El algoritmo de Score forma parte de la estrategia.

Como principio permanente:

- cada operación identificará el modelo de Score utilizado;
- las modificaciones del algoritmo deberán conservar la comparabilidad histórica;
- los distintos modelos podrán coexistir dentro del mismo histórico.

La evolución del Score deberá evaluarse mediante evidencia estadística.

---

# 12.7 Metodología

La metodología oficial del proyecto establece que:

- ninguna estrategia se modificará por intuición;
- ninguna versión se adoptará sin evidencia suficiente;
- toda optimización deberá ser cuantificable;
- la evidencia tendrá prioridad sobre cualquier percepción subjetiva.

Este principio constituye el fundamento metodológico del proyecto.

---

# 12.8 Desarrollo

El orden oficial de prioridades será siempre:

1. Correctitud funcional.
2. Integridad de los datos.
3. Estabilidad.
4. Calidad arquitectónica.
5. Evidencia estadística.
6. Rendimiento.
7. Incorporación de nuevas funcionalidades.

Ninguna nueva capacidad justificará comprometer alguno de los principios anteriores.

---

# 12.9 Visión de Largo Plazo

El Proyecto Bots Binance evolucionará como una plataforma de investigación cuantitativa.

Toda nueva herramienta deberá integrarse reutilizando la arquitectura existente y respetando los principios definidos en este Documento Maestro.

La estabilidad de la plataforma tendrá siempre prioridad sobre el crecimiento acelerado de funcionalidades.

# 13. Próximos Hitos

Los siguientes hitos representan el orden oficial de evolución del Proyecto Bots Binance.

Su finalidad es consolidar progresivamente las capacidades de la plataforma respetando la arquitectura y la metodología definidas en este Documento Maestro.

Las prioridades podrán ajustarse conforme evolucione el proyecto, siempre que no comprometan la estabilidad ni la comparabilidad de la evidencia histórica.

---

# 13.1 Prioridad Inmediata

## Consolidación del Analizador de Estadísticas v1.0

Objetivo:

Completar oficialmente la primera versión estable del Analizador mediante la incorporación del módulo de Hallazgos Estratégicos.

Este módulo deberá:

- reutilizar las métricas existentes;
- consumir el Diagnóstico Automático y el Motor de Evidencia;
- generar conclusiones automáticas;
- no recalcular indicadores ya obtenidos por el Motor Estadístico.

Con este desarrollo quedará oficialmente finalizada la versión 1.0 del Analizador.

---

# 13.2 Prioridad Alta

## Comparador Automático entre Versiones

Objetivo:

Desarrollar un módulo capaz de comparar distintas versiones de una estrategia utilizando una metodología homogénea.

Entre sus capacidades previstas:

- comparación de métricas;
- comparación de evidencia;
- comparación de diagnósticos;
- comparación de hallazgos;
- generación de conclusiones automáticas.

Este componente reutilizará íntegramente la arquitectura del Analizador.

---

## Finalización de la Validación del Bot TradFi

Objetivo:

Completar la muestra estadística necesaria para evaluar objetivamente la estrategia implementada.

La transición hacia producción únicamente podrá considerarse cuando la evidencia obtenida demuestre un comportamiento consistente y compatible con los criterios definidos por la metodología del proyecto.

---

# 13.3 Prioridad Media

## Evolución Controlada de Estrategias

Una vez concluida la validación estadística, podrán iniciarse investigaciones orientadas a:

- optimización de filtros;
- gestión dinámica del riesgo;
- incorporación de nuevos indicadores;
- evaluación de nuevos modelos de Score;
- mejoras en la selección de oportunidades.

Cada modificación deberá implementarse como una nueva versión de estrategia y compararse objetivamente con la versión anterior.

---

## Análisis Integral de Señales

El análisis de `senales_detectadas.csv` se desarrollará durante la Fase 2 del proyecto.

Previamente será necesario modificar el proceso de registro para almacenar todas las oportunidades detectadas antes de aplicar el límite de posiciones simultáneas.

Solo entonces será posible evaluar objetivamente el desempeño del algoritmo de priorización.

---

# 13.4 Prioridad Estratégica

## Backtesting

Desarrollar un entorno reutilizable para validar nuevas estrategias antes de incorporarlas a los bots operativos.

Este componente compartirá la misma arquitectura analítica utilizada por el Analizador de Estadísticas.

---

## Automatización

Incorporar herramientas que reduzcan progresivamente la intervención manual durante el proceso de investigación.

Entre ellas:

- generación automática de reportes;
- dashboards;
- monitoreo;
- exportación de resultados;
- alertas automáticas.

---

## Infraestructura

Migrar progresivamente la plataforma hacia una infraestructura de alta disponibilidad capaz de soportar la operación continua de todos los componentes del proyecto.

---

# 13.5 Visión de Largo Plazo

El objetivo final consiste en disponer de una plataforma integrada capaz de:

- desarrollar nuevas estrategias;
- validarlas estadísticamente;
- compararlas objetivamente;
- desplegarlas en producción;
- supervisarlas continuamente;
- preservar toda la evidencia histórica generada durante su evolución.

Cada hito alcanzado deberá fortalecer la plataforma sin alterar los principios arquitectónicos establecidos en este Documento Maestro.

# 14. Conclusión

El presente documento constituye la especificación arquitectónica oficial del Proyecto Bots Binance.

Su finalidad es preservar, documentar y comunicar los principios que gobiernan la evolución de la plataforma, garantizando que todas las decisiones técnicas mantengan coherencia con la arquitectura, la metodología de validación estadística y los objetivos estratégicos del proyecto.

Este documento representa la referencia principal para comprender:

- la arquitectura general de la plataforma;
- la función de cada componente;
- la metodología oficial de investigación cuantitativa;
- los principios de evolución de las estrategias;
- las decisiones técnicas consolidadas;
- la hoja de ruta del proyecto.

---

# 14.1 Función del Documento Maestro

El Documento Maestro cumple cinco funciones principales.

## Especificación Arquitectónica

Describe la estructura oficial de la plataforma y define las responsabilidades de cada componente.

---

## Registro de Decisiones

Documenta las decisiones técnicas y metodológicas que se consideran permanentes dentro del proyecto.

---

## Referencia de Continuidad

Permite retomar el desarrollo del proyecto en cualquier momento sin perder el contexto arquitectónico acumulado.

Toda nueva sesión de trabajo deberá utilizar este documento como referencia principal.

---

## Guía para la Evolución

Establece el marco metodológico que deberá seguir cualquier modificación futura de la plataforma.

Las nuevas funcionalidades deberán integrarse respetando los principios aquí definidos.

---

## Base para la Investigación

Constituye el marco de referencia para el proceso de investigación cuantitativa desarrollado por el proyecto.

Toda evolución de las estrategias deberá mantenerse alineada con la Metodología de Validación Estadística documentada en este archivo.

---

# 14.2 Principios Permanentes

El crecimiento del Proyecto Bots Binance deberá respetar permanentemente los siguientes principios:

- arquitectura modular;
- separación de responsabilidades;
- integridad del histórico;
- comparabilidad entre versiones;
- evidencia estadística como criterio de decisión;
- evolución incremental;
- estabilidad antes que complejidad.

Estos principios tienen prioridad sobre cualquier decisión puntual de implementación.

---

# 14.3 Filosofía de Evolución

La evolución del proyecto seguirá siempre el mismo proceso:

```text
Diseñar

↓

Implementar

↓

Validar

↓

Medir

↓

Analizar

↓

Obtener Evidencia

↓

Generar Hallazgos

↓

Optimizar

↓

Comparar

↓

Repetir
```

Cada iteración deberá producir conocimiento que permita mejorar la siguiente versión de la estrategia.

El éxito del proyecto dependerá de la disciplina para respetar este proceso y de la capacidad para tomar decisiones fundamentadas en evidencia objetiva.

---

# 14.4 Visión Final

El objetivo de largo plazo del Proyecto Bots Binance no consiste únicamente en desarrollar bots de trading.

El propósito es construir una plataforma integral de investigación cuantitativa capaz de diseñar, validar, comparar y evolucionar estrategias de forma reproducible, trazable y estadísticamente sustentada.

La rentabilidad constituye una consecuencia deseable del proceso, pero nunca sustituirá a la metodología.

Mientras la arquitectura y la metodología permanezcan sólidas, la plataforma podrá incorporar nuevos mercados, nuevas estrategias y nuevas tecnologías sin perder coherencia.

Este Documento Maestro deberá evolucionar junto con la plataforma, preservando siempre los principios fundamentales que dieron origen al proyecto.

# Anexo A – Registro de Cambios

El presente anexo documenta la evolución del Documento Maestro del Proyecto Bots Binance.

Su objetivo es preservar la trazabilidad de las decisiones arquitectónicas incorporadas a lo largo del desarrollo del proyecto.

---

## Versión 2.0 (Junio 2026)

Principales cambios:

- Reestructuración completa del Documento Maestro.
- Definición de la arquitectura modular del proyecto.
- Documentación independiente del Bot Crypto y Bot TradFi.
- Incorporación del Sistema de Estadísticas.
- Incorporación del Analizador de Estadísticas.
- Definición formal de la Metodología de Validación Estadística.
- Consolidación de las decisiones técnicas principales.
- Definición del Roadmap del proyecto.

---

## Versión 2.2 (Julio 2026)

La presente versión representa una actualización arquitectónica del proyecto.

Principales cambios:

### Arquitectura

- Reorganización completa del documento bajo un enfoque de plataforma de investigación cuantitativa.
- Separación explícita entre arquitectura permanente y planificación evolutiva.
- Definición formal de las capas arquitectónicas de la plataforma.
- Consolidación del Analizador como núcleo de inteligencia cuantitativa.

### Bots

- Actualización de la versión oficial del Bot Crypto a Fase1.1_MACD_BTC1H.
- Actualización de la versión oficial del Bot TradFi a Fase1.2_MACD_QQQ1H.
- Documentación del modelo de Score NORMALIZADO_V1.
- Formalización del concepto de modelo de Score versionable.

### Sistema de Estadísticas

- Redefinición como repositorio oficial de evidencia.
- Incorporación del principio de comparabilidad histórica.
- Actualización del papel del archivo senales_detectadas.csv.
- Formalización del registro de versión y modelo de Score.

### Analizador

- Consolidación de la arquitectura v1.0.
- Documentación del Motor Estadístico.
- Incorporación del Diagnóstico Automático.
- Incorporación del Motor de Evidencia.
- Definición del módulo Hallazgos Estratégicos.
- Preparación arquitectónica para el Comparador de Estrategias.

### Metodología

- Consolidación de la evidencia estadística como criterio oficial de decisión.
- Incorporación de la comparación entre versiones como parte del proceso de evolución.
- Definición del ciclo oficial de investigación cuantitativa.

### Roadmap

- Sustitución del esquema rígido por fases por líneas independientes de evolución.
- Reorganización de los objetivos estratégicos de la plataforma.

Esta versión sustituye completamente a la versión 2.0 y pasa a constituir la referencia oficial del proyecto.

# Anexo B – Convenciones del Proyecto

El presente anexo define las convenciones oficiales utilizadas durante el desarrollo del Proyecto Bots Binance.

Su finalidad es preservar la consistencia entre versiones, facilitar la trazabilidad y garantizar la comparabilidad de la información histórica.

---

## B.1 Versionado de Estrategias

Toda modificación que altere el comportamiento operativo de un bot deberá generar una nueva versión de estrategia.

Ejemplos:

```text
Fase1.0_MACD_BTC1H

↓

Fase1.1_MACD_BTC1H

↓

Fase1.2_MACD_BTC1H
```

Las versiones anteriores permanecerán documentadas y serán comparables mediante el Analizador.

---

## B.2 Versionado del Modelo de Score

El algoritmo de Score constituye un componente independiente de la estrategia.

Cada modificación relevante deberá identificarse mediante un nuevo modelo.

Ejemplos:

```text
ORIGINAL_V1

NORMALIZADO_V1

NORMALIZADO_V2
```

El modelo utilizado deberá almacenarse en cada operación.

---

## B.3 Compatibilidad

Toda evolución deberá preservar la posibilidad de analizar información histórica.

Como principio general:

- no se eliminarán columnas existentes;
- la nueva información se añadirá mediante nuevos campos;
- el Analizador deberá mantener compatibilidad con versiones anteriores siempre que resulte técnicamente viable.

---

## B.4 Actualización del Documento Maestro

El Documento Maestro deberá actualizarse cuando ocurra alguno de los siguientes eventos:

- incorporación de nuevos componentes arquitectónicos;
- modificación permanente de la metodología;
- cambios en la arquitectura general;
- consolidación de nuevas decisiones técnicas;
- cambios relevantes en el flujo oficial del proyecto.

Las correcciones menores de código no requieren modificar este documento.

---

## B.5 Filosofía de Desarrollo

Durante todo el proyecto se mantendrá el siguiente orden de prioridades:

1. Correctitud funcional.
2. Integridad de los datos.
3. Estabilidad.
4. Calidad arquitectónica.
5. Evidencia estadística.
6. Rendimiento.
7. Nuevas funcionalidades.

Esta jerarquía constituye la guía oficial para la toma de decisiones técnicas.