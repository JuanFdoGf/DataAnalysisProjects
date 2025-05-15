# 📊 DataAnalysisProjects

## Descripción general

Este repositorio alberga una colección de proyectos de análisis de datos orientados a fortalecer competencias prácticas en:

- **Limpieza y preprocesamiento de datos**: validación, imputación, normalización y detección de valores atípicos.
- **Análisis exploratorio de datos (EDA)**: generación de métricas estadísticas y visualizaciones avanzadas para identificar patrones relevantes.
- **Feature Engineering**: creación y selección de variables que maximicen la calidad del modelo y la interpretabilidad de los resultados.
- **Visualización interactiva**: desarrollo de dashboards y gráficos con Plotly, Dash o Streamlit para comunicar hallazgos a audiencias técnicas y de negocio.

Cada proyecto incluye documentación detallada que respalda cada decisión técnica y facilita la reproducibilidad del análisis.

---

## 🚀 Objetivos del repositorio

1. **Dominar técnicas de EDA** mediante pandas, NumPy y matplotlib.
2. **Optimizar pipelines de datos** con transformaciones avanzadas y prácticas de ingeniería de datos reproducibles.
3. **Aplicar análisis estadístico descriptivo y modelado** (regresión lineal, pruebas de hipótesis, correlaciones multivariadas).
4. **Implementar dashboards interactivos** para visualización y exploración de resultados.
5. **Explorar casos de uso reales** en series de tiempo, análisis geoespacial y detección de anomalías.

---

## 🗂 Estructura de carpetas

```
DataAnalysisProjects/
│
├── project_01_eda_sales_data/
│   ├── data/                  # Datos originales y procesados
│   ├── notebooks/             # Jupyter notebooks con análisis paso a paso
│   ├── src/                   # Módulos y scripts Python reutilizables
│   ├── reports/               # Gráficos estáticos y archivos de salida
│   └── README.md              # Descripción específica y resultados clave
│
├── project_02_time_series/
│   ├── data/
│   ├── notebooks/
│   ├── src/
│   ├── reports/
│   └── README.md
│
├── project_03_geospatial_analysis/
│   └── …
│
├── project_04_iot_anomaly_detection/
│   └── …
│
└── README.md                  # Archivo de presentación general
```

---

## 📁 Proyectos sugeridos

1. **Análisis de ventas minoristas**
   - **Objetivo**: Identificar patrones estacionales y segmentar clientes.
   - **Tecnologías**: pandas, seaborn, scikit-learn (K-Means, DBSCAN).

2. **Series de tiempo financieras**
   - **Objetivo**: Modelar y pronosticar ventas diarias.
   - **Tecnologías**: statsmodels (ARIMA), Prophet, evaluación con backtesting.

3. **Análisis geoespacial de movilidad urbana**
   - **Objetivo**: Visualizar flujos de transporte y densidad de puntos.
   - **Tecnologías**: GeoPandas, folium, heatmaps.

4. **Detección de anomalías en datos de IoT**
   - **Objetivo**: Reconocer eventos atípicos en series de sensores.
   - **Tecnologías**: rolling statistics, z-score, Isolation Forest.

5. **Dashboard interactivo de exploración**
   - **Objetivo**: Crear una interfaz para el análisis de cualquier proyecto.
   - **Tecnologías**: Plotly Dash, Streamlit, despliegue en Heroku/AWS.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para colaborar:

1. Abre un **issue** describiendo tu propuesta.
2. Haz un **fork** del repositorio.
3. Crea una rama (`git checkout -b feature/nombre`).
4. Realiza tus cambios y commitea (`git commit -m 'feat: descripción'`).
5. Envía un **pull request** y espera revisión.

---

## 📚 Referencias y recursos

- **Wes McKinney**, *Python for Data Analysis*.
- **Stefanie Molin**, *Hands-On Data Analysis with Pandas*.
- Documentación oficial de pandas, NumPy, GeoPandas, Plotly, Prophet y scikit-learn.
