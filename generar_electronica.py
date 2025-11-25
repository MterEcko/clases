#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Curso de Electrónica
3 versiones: 9-13 años, 14-18 años, 15+ años
"""

from generador_cursos import GeneradorCurso


# ============================================================================
# CURSO DE ELECTRÓNICA - 9 A 13 AÑOS
# ============================================================================

electronica_9_13 = {
    'nombre': 'Curso de Electrónica Básica',
    'grupo_edad': '9-13 años',
    'duracion_sesion': '1 hora',
    'nivel': 'Principiante',
    'precio_curso': 2400.00,
    'costo_materiales': 850.00,
    'ruta': 'cursos/01-Electronica/9-13-años',

    'descripcion': '''
    Este curso introduce a los niños al fascinante mundo de la electrónica de manera
    práctica y divertida. A través de experimentos simples y proyectos emocionantes,
    los estudiantes aprenderán los conceptos básicos de electricidad, circuitos y
    componentes electrónicos. El curso está diseñado para despertar la curiosidad y
    fomentar el pensamiento lógico mediante actividades hands-on.
    ''',

    'objetivos': [
        'Comprender los conceptos básicos de electricidad y circuitos',
        'Identificar y utilizar componentes electrónicos simples (LEDs, resistencias, switches)',
        'Construir circuitos básicos en protoboard',
        'Leer diagramas de circuitos simples',
        'Desarrollar habilidades de resolución de problemas',
        'Crear proyectos electrónicos funcionales'
    ],

    'requisitos': [
        'Ninguno - curso diseñado para principiantes absolutos',
        'Curiosidad por aprender',
        'Materiales del curso (incluidos en el kit)'
    ],

    'modulos': [
        {
            'nombre': 'Introducción a la Electricidad',
            'sesiones': '1-4',
            'descripcion': 'Conceptos fundamentales de electricidad, seguridad y primeros experimentos',
            'contenido_detallado': [
                {
                    'titulo': '¿Qué es la electricidad?',
                    'puntos': ['Electricidad en la vida diaria', 'Átomos y electrones (concepto simple)',
                              'Conductores y aislantes', 'Seguridad eléctrica']
                }
            ]
        },
        {
            'nombre': 'Componentes Electrónicos Básicos',
            'sesiones': '5-10',
            'descripcion': 'Conocer y experimentar con LEDs, resistencias, switches y baterías',
            'contenido_detallado': [
                {
                    'titulo': 'Componentes esenciales',
                    'puntos': ['LEDs y su funcionamiento', 'Resistencias y código de colores',
                              'Switches y botones', 'Baterías y fuentes de poder']
                }
            ]
        },
        {
            'nombre': 'Circuitos Simples',
            'sesiones': '11-16',
            'descripcion': 'Construcción de circuitos básicos y uso del protoboard',
            'contenido_detallado': [
                {
                    'titulo': 'Construyendo circuitos',
                    'puntos': ['Circuitos en serie', 'Circuitos en paralelo',
                              'Uso del protoboard', 'Lectura de diagramas']
                }
            ]
        },
        {
            'nombre': 'Proyectos Divertidos',
            'sesiones': '17-24',
            'descripcion': 'Crear proyectos electrónicos funcionales y proyecto final',
            'contenido_detallado': [
                {
                    'titulo': 'Proyectos creativos',
                    'puntos': ['Alarma simple', 'Lámpara LED multicolor',
                              'Semáforo', 'Proyecto final personalizado']
                }
            ]
        }
    ],

    'sesiones': [
        # Módulo 1: Introducción a la Electricidad
        {
            'titulo': 'Bienvenida y ¿Qué es la Electricidad?',
            'objetivos': ['Conocer a los compañeros', 'Entender qué es la electricidad',
                         'Identificar aparatos eléctricos en casa'],
            'contenido': ['Presentación del curso', 'Electricidad en la vida diaria',
                         'Demostración de electricidad estática'],
            'actividades': 'Experimento de globo y cabello (electricidad estática), dibujar aparatos eléctricos',
            'materiales': 'Globos, papeles pequeños, pizarra'
        },
        {
            'titulo': 'Seguridad Eléctrica',
            'objetivos': ['Aprender reglas de seguridad', 'Identificar peligros eléctricos'],
            'contenido': ['Reglas de oro de seguridad', 'Qué nunca hacer con electricidad',
                         'Señales de peligro'],
            'actividades': 'Juego de identificar situaciones seguras/peligrosas, crear carteles de seguridad',
            'materiales': 'Cartulinas, marcadores, imágenes impresas'
        },
        {
            'titulo': 'Conductores y Aislantes',
            'objetivos': ['Diferenciar materiales conductores y aislantes', 'Experimentar con diferentes materiales'],
            'contenido': ['Qué son conductores', 'Qué son aislantes', 'Ejemplos cotidianos'],
            'actividades': 'Experimento con circuito simple y diferentes materiales para probar conductividad',
            'materiales': 'Batería, LED, cables, objetos diversos (monedas, plástico, madera, metal)'
        },
        {
            'titulo': 'Circuito Básico con Batería y LED',
            'objetivos': ['Construir primer circuito funcional', 'Entender flujo de corriente'],
            'contenido': ['Partes de un circuito', 'Símbolo de batería y LED', 'Flujo de corriente'],
            'actividades': 'Construir circuito simple: batería + LED usando caimanes',
            'materiales': 'Baterías 9V, LEDs, clips caimán'
        },

        # Módulo 2: Componentes Electrónicos Básicos
        {
            'titulo': 'Conociendo el LED',
            'objetivos': ['Entender cómo funciona un LED', 'Identificar ánodo y cátodo'],
            'contenido': ['¿Qué es un LED?', 'Partes del LED', 'Polaridad del LED', 'Colores de LEDs'],
            'actividades': 'Encender LEDs de diferentes colores, identificar patas largo/corto',
            'materiales': 'LEDs variados, baterías, resistencias'
        },
        {
            'titulo': 'La Resistencia - Control de Corriente',
            'objetivos': ['Entender para qué sirve una resistencia', 'Aprender código de colores básico'],
            'contenido': ['Función de la resistencia', 'Código de colores (simplificado)',
                         'Por qué proteger el LED'],
            'actividades': 'Comparar LED con/sin resistencia (demo del profesor), identificar colores',
            'materiales': 'Resistencias varias, tabla de colores impresa, LEDs'
        },
        {
            'titulo': 'Switches y Botones',
            'objetivos': ['Aprender a usar switches', 'Controlar circuitos'],
            'contenido': ['Tipos de switches', 'Switches ON/OFF', 'Botones pulsadores', 'Aplicaciones'],
            'actividades': 'Crear circuito con switch para controlar LED',
            'materiales': 'Switches, botones, baterías, LEDs'
        },
        {
            'titulo': 'Baterías y Pilas',
            'objetivos': ['Entender tipos de baterías', 'Aprender sobre voltaje básico'],
            'contenido': ['Tipos de baterías', 'Voltaje (concepto simple)', 'Duración y cuidado'],
            'actividades': 'Comparar diferentes baterías, medir duración con cronómetro',
            'materiales': 'Baterías AA, AAA, 9V, porta baterías'
        },
        {
            'titulo': 'Introducción al Protoboard',
            'objetivos': ['Conocer el protoboard', 'Entender cómo están conectados los puntos'],
            'contenido': ['¿Qué es el protoboard?', 'Filas y columnas', 'Conexiones internas',
                         'Ventajas del protoboard'],
            'actividades': 'Explorar protoboard con tester (demo), insertar componentes',
            'materiales': 'Protoboards, cables, LEDs, resistencias'
        },
        {
            'titulo': 'Primer Circuito en Protoboard',
            'objetivos': ['Construir circuito completo en protoboard', 'Seguir diagrama simple'],
            'contenido': ['Diagrama de circuito', 'Paso a paso del montaje', 'Verificación del circuito'],
            'actividades': 'Construir circuito: batería + resistencia + LED en protoboard',
            'materiales': 'Kit completo (protoboard, batería, resistencia, LED, cables)'
        },

        # Módulo 3: Circuitos Simples
        {
            'titulo': 'Circuitos en Serie - Parte 1',
            'objetivos': ['Entender qué es un circuito en serie', 'Construir circuito con 2 LEDs en serie'],
            'contenido': ['Definición de serie', 'Características', 'Voltaje en serie', 'Diagrama'],
            'actividades': 'Construir circuito con 2 LEDs en serie, observar brillo',
            'materiales': 'Protoboard, 2 LEDs, resistencias, batería 9V'
        },
        {
            'titulo': 'Circuitos en Serie - Parte 2',
            'objetivos': ['Experimentar con más LEDs en serie', 'Observar efecto en el brillo'],
            'contenido': ['Agregar más LEDs', 'Caída de voltaje', '¿Qué pasa si uno falla?'],
            'actividades': 'Construir serie de 3-4 LEDs, quitar uno y observar',
            'materiales': 'Protoboard, 4 LEDs, resistencias, batería'
        },
        {
            'titulo': 'Circuitos en Paralelo - Parte 1',
            'objetivos': ['Entender qué es un circuito en paralelo', 'Construir circuito con 2 LEDs en paralelo'],
            'contenido': ['Definición de paralelo', 'Características', 'Voltaje en paralelo', 'Diagrama'],
            'actividades': 'Construir circuito con 2 LEDs en paralelo, comparar con serie',
            'materiales': 'Protoboard, 2 LEDs, resistencias, batería'
        },
        {
            'titulo': 'Circuitos en Paralelo - Parte 2',
            'objetivos': ['Experimentar con más LEDs en paralelo', 'Comparar serie vs paralelo'],
            'contenido': ['Agregar más LEDs en paralelo', '¿Qué pasa si uno falla?', 'Ventajas/desventajas'],
            'actividades': 'Construir paralelo de 3 LEDs, quitar uno y observar diferencia con serie',
            'materiales': 'Protoboard, 3 LEDs, resistencias, batería'
        },
        {
            'titulo': 'Circuitos Mixtos',
            'objetivos': ['Combinar serie y paralelo', 'Crear circuitos más complejos'],
            'contenido': ['Serie + paralelo combinados', 'Planificar circuito', 'Resolución de problemas'],
            'actividades': 'Diseñar y construir circuito mixto con 4 LEDs',
            'materiales': 'Protoboard, 4 LEDs, resistencias, batería'
        },
        {
            'titulo': 'Control de Circuitos con Switches',
            'objetivos': ['Agregar control a circuitos', 'Crear circuitos interactivos'],
            'contenido': ['Switches en circuitos', 'Control independiente', 'Aplicaciones prácticas'],
            'actividades': 'Construir circuito con 2 switches para controlar LEDs independientemente',
            'materiales': 'Protoboard, LEDs, switches, resistencias, batería'
        },

        # Módulo 4: Proyectos Divertidos
        {
            'titulo': 'Proyecto: Linterna LED',
            'objetivos': ['Crear proyecto funcional', 'Aplicar conocimientos'],
            'contenido': ['Planificación del proyecto', 'Selección de componentes', 'Ensamblaje'],
            'actividades': 'Construir linterna LED con switch y porta batería',
            'materiales': 'LED blanco potente, switch, porta batería, resistencia, caja pequeña'
        },
        {
            'titulo': 'Proyecto: Luz de Emergencia',
            'objetivos': ['Crear circuito con múltiples LEDs', 'Aplicar paralelo/serie'],
            'contenido': ['Diseño de luz de emergencia', 'Optimización de batería', 'Decoración'],
            'actividades': 'Construir luz con 6 LEDs en paralelo, decorar carcasa',
            'materiales': 'Protoboard, 6 LEDs, resistencias, switch, batería 9V, caja'
        },
        {
            'titulo': 'Proyecto: Semáforo Electrónico',
            'objetivos': ['Crear semáforo funcional', 'Usar LEDs de colores'],
            'contenido': ['Secuencia de semáforo', 'Control manual', 'Montaje vertical'],
            'actividades': 'Construir semáforo con LEDs rojo-amarillo-verde y switches',
            'materiales': 'LEDs (rojo, amarillo, verde), 3 switches, resistencias, protoboard, cartón'
        },
        {
            'titulo': 'Proyecto: Tarjeta LED Luminosa',
            'objetivos': ['Crear circuito decorativo', 'Combinar electrónica con arte'],
            'contenido': ['Circuitos en papel', 'Cinta de cobre', 'Diseño creativo'],
            'actividades': 'Crear tarjeta con circuito de LEDs integrado',
            'materiales': 'Cartulina, cinta de cobre, LEDs, batería de botón, decoraciones'
        },
        {
            'titulo': 'Proyecto: Juego de Preguntas',
            'objetivos': ['Crear juego interactivo', 'Aplicar switches'],
            'contenido': ['Circuito de prueba', 'Conexiones correctas/incorrectas', 'LED indicador'],
            'actividades': 'Construir juego donde LED enciende si conexión es correcta',
            'materiales': 'Protoboard, cables, LEDs, switches, cartulina para preguntas'
        },
        {
            'titulo': 'Introducción al Proyecto Final',
            'objetivos': ['Elegir proyecto personal', 'Planificar construcción'],
            'contenido': ['Ideas de proyectos', 'Recursos disponibles', 'Plan de trabajo'],
            'actividades': 'Cada alumno elige y dibuja su proyecto final',
            'materiales': 'Papel, lápices de colores, catálogo de componentes'
        },
        {
            'titulo': 'Construcción del Proyecto Final - Día 1',
            'objetivos': ['Iniciar proyecto final', 'Construir circuito base'],
            'contenido': ['Verificación de componentes', 'Ensamblaje inicial', 'Pruebas'],
            'actividades': 'Trabajar en proyecto personal con guía del instructor',
            'materiales': 'Componentes según proyecto de cada alumno'
        },
        {
            'titulo': 'Construcción del Proyecto Final - Día 2 y Presentación',
            'objetivos': ['Completar proyecto', 'Presentar a compañeros', 'Celebrar logros'],
            'contenido': ['Finalización', 'Decoración', 'Preparar presentación', 'Compartir'],
            'actividades': 'Completar proyecto, presentar funcionamiento, votación del más creativo',
            'materiales': 'Componentes finales, materiales de decoración, diplomas'
        }
    ],

    'evaluacion': {
        'descripcion': '''
        La evaluación es continua y formativa, enfocada en el proceso de aprendizaje más que
        en calificaciones numéricas. Se valora la participación, curiosidad, trabajo en equipo
        y esfuerzo en los proyectos.
        ''',
        'criterios': {
            'Participación en clase y experimentos': '20%',
            'Construcción correcta de circuitos (sesiones prácticas)': '30%',
            'Proyectos intermedios': '20%',
            'Proyecto final': '30%'
        }
    },

    'proyecto_final': {
        'titulo': 'Mi Invento Electrónico',
        'descripcion': '''
        Los estudiantes crearán un proyecto electrónico personalizado aplicando todo lo aprendido.
        Puede ser una lámpara decorativa, juego, dispositivo útil, o cualquier invención creativa
        que incluya circuitos con LEDs, switches y los componentes vistos en clase.
        ''',
        'entregables': [
            'Circuito funcional en protoboard o ensamblaje final',
            'Dibujo del circuito (diagrama simple)',
            'Breve presentación oral explicando cómo funciona (2 minutos)',
            'Decoración o carcasa creativa'
        ]
    },

    'materiales': [
        {'cantidad': 1, 'nombre': 'Protoboard 400 puntos', 'descripcion': 'Tableta de prototipado',
         'precio_unitario': 80.00},
        {'cantidad': 1, 'nombre': 'Kit de LEDs (50 pzs)', 'descripcion': 'LEDs variados 5mm',
         'precio_unitario': 120.00},
        {'cantidad': 1, 'nombre': 'Kit de resistencias', 'descripcion': '100 resistencias variadas',
         'precio_unitario': 50.00},
        {'cantidad': 5, 'nombre': 'Baterías 9V', 'descripcion': 'Baterías alcalinas',
         'precio_unitario': 35.00},
        {'cantidad': 1, 'nombre': 'Porta baterías 9V', 'descripcion': 'Con cables',
         'precio_unitario': 25.00},
        {'cantidad': 10, 'nombre': 'Cables jumper', 'descripcion': 'Cables macho-macho 20cm',
         'precio_unitario': 2.00},
        {'cantidad': 5, 'nombre': 'Switches ON/OFF', 'descripcion': 'Interruptores pequeños',
         'precio_unitario': 8.00},
        {'cantidad': 3, 'nombre': 'Botones pulsadores', 'descripcion': 'Push buttons',
         'precio_unitario': 5.00},
        {'cantidad': 1, 'nombre': 'Porta baterías AA (4x)', 'descripcion': 'Con cables',
         'precio_unitario': 30.00},
        {'cantidad': 8, 'nombre': 'Baterías AA', 'descripcion': 'Alcalinas',
         'precio_unitario': 12.00},
        {'cantidad': 1, 'nombre': 'Kit de clips caimán', 'descripcion': '10 cables con pinzas',
         'precio_unitario': 60.00},
        {'cantidad': 1, 'nombre': 'Cinta de cobre', 'descripcion': 'Rollo 5mm x 10m',
         'precio_unitario': 85.00},
        {'cantidad': 1, 'nombre': 'Material de arte', 'descripcion': 'Cartulinas, marcadores, pegamento',
         'precio_unitario': 120.00}
    ]
}


# ============================================================================
# CURSO DE ELECTRÓNICA - 14 A 18 AÑOS
# ============================================================================

electronica_14_18 = {
    'nombre': 'Curso de Electrónica Práctica',
    'grupo_edad': '14-18 años',
    'duracion_sesion': '1.5 horas',
    'nivel': 'Intermedio',
    'precio_curso': 3200.00,
    'costo_materiales': 1350.00,
    'ruta': 'cursos/01-Electronica/14-18-años',

    'descripcion': '''
    Este curso proporciona una base sólida en electrónica analógica y digital, combinando
    teoría con práctica intensiva. Los estudiantes aprenderán a diseñar, construir y
    analizar circuitos electrónicos, utilizando componentes como transistores, capacitores,
    y circuitos integrados básicos. Ideal para quienes buscan entender la tecnología desde
    sus fundamentos.
    ''',

    'objetivos': [
        'Dominar los fundamentos de electricidad y magnetismo',
        'Analizar circuitos usando Ley de Ohm y leyes de Kirchhoff',
        'Trabajar con componentes activos (transistores, diodos)',
        'Diseñar y construir circuitos analógicos y digitales básicos',
        'Utilizar multímetro y osciloscopio básico',
        'Leer e interpretar datasheets de componentes',
        'Desarrollar proyectos electrónicos funcionales'
    ],

    'requisitos': [
        'Conocimientos básicos de matemáticas (álgebra)',
        'Interés en tecnología y electrónica',
        'Materiales del curso (incluidos)'
    ],

    'modulos': [
        {
            'nombre': 'Fundamentos de Electricidad y Medición',
            'sesiones': '1-6',
            'descripcion': 'Conceptos eléctricos fundamentales, leyes básicas y uso de instrumentos',
            'contenido_detallado': [
                {
                    'titulo': 'Teoría eléctrica',
                    'puntos': ['Voltaje, corriente y resistencia', 'Ley de Ohm',
                              'Potencia eléctrica', 'Uso del multímetro']
                }
            ]
        },
        {
            'nombre': 'Componentes Pasivos y Activos',
            'sesiones': '7-12',
            'descripcion': 'Resistencias, capacitores, inductores, diodos y transistores',
            'contenido_detallado': [
                {
                    'titulo': 'Componentes esenciales',
                    'puntos': ['Resistencias variables', 'Capacitores y su función',
                              'Diodos y rectificación', 'Transistores como switch']
                }
            ]
        },
        {
            'nombre': 'Circuitos Analógicos',
            'sesiones': '13-18',
            'descripcion': 'Amplificadores, filtros, osciladores y fuentes de alimentación',
            'contenido_detallado': [
                {
                    'titulo': 'Aplicaciones analógicas',
                    'puntos': ['Amplificadores con transistores', 'Fuentes reguladas',
                              'Osciladores', 'Filtros RC']
                }
            ]
        },
        {
            'nombre': 'Electrónica Digital y Proyectos',
            'sesiones': '19-24',
            'descripcion': 'Compuertas lógicas, circuitos integrados y proyecto final',
            'contenido_detallado': [
                {
                    'titulo': 'Digital y proyectos',
                    'puntos': ['Compuertas lógicas', 'Circuitos integrados (555, op-amps)',
                              'Proyectos integrados', 'Diseño personalizado']
                }
            ]
        }
    ],

    'sesiones': [
        # Módulo 1
        {
            'titulo': 'Introducción y Conceptos Básicos',
            'objetivos': ['Comprender voltaje, corriente y resistencia', 'Entender la Ley de Ohm'],
            'contenido': ['Historia de la electrónica', 'Magnitudes eléctricas', 'Ley de Ohm',
                         'Ejercicios de cálculo'],
            'actividades': 'Resolución de problemas con Ley de Ohm, simulaciones',
            'materiales': 'Calculadora, pizarra, software de simulación (opcional)'
        },
        {
            'titulo': 'Uso del Multímetro',
            'objetivos': ['Manejar multímetro correctamente', 'Medir voltaje, corriente y resistencia'],
            'contenido': ['Partes del multímetro', 'Modo voltímetro', 'Modo amperímetro',
                         'Modo óhmetro', 'Precauciones'],
            'actividades': 'Práctica de mediciones en circuitos simples, medir componentes',
            'materiales': 'Multímetros, baterías, resistencias, LEDs'
        },
        {
            'titulo': 'Circuitos Serie y Paralelo',
            'objetivos': ['Analizar circuitos serie y paralelo', 'Calcular resistencias equivalentes'],
            'contenido': ['Resistencias en serie', 'Resistencias en paralelo', 'Circuitos mixtos',
                         'Divisores de voltaje'],
            'actividades': 'Construcción y medición de circuitos, verificar cálculos',
            'materiales': 'Protoboard, resistencias variadas, fuente de alimentación, multímetro'
        },
        {
            'titulo': 'Leyes de Kirchhoff',
            'objetivos': ['Aplicar leyes de Kirchhoff', 'Resolver circuitos complejos'],
            'contenido': ['Ley de corrientes (LCK)', 'Ley de voltajes (LVK)', 'Análisis de mallas',
                         'Análisis de nodos'],
            'actividades': 'Resolver circuitos en papel y verificar en protoboard',
            'materiales': 'Protoboard, componentes variados, multímetro'
        },
        {
            'titulo': 'Potencia Eléctrica',
            'objetivos': ['Calcular potencia eléctrica', 'Dimensionar componentes'],
            'contenido': ['Fórmulas de potencia', 'Disipación de calor', 'Selección de resistencias',
                         'Eficiencia'],
            'actividades': 'Cálculos de potencia, medición de temperatura en resistencias',
            'materiales': 'Resistencias de potencia, multímetro, termómetro IR'
        },
        {
            'titulo': 'Código de Colores y Lectura de Esquemas',
            'objetivos': ['Dominar código de colores', 'Leer diagramas esquemáticos'],
            'contenido': ['Código de colores 4 y 5 bandas', 'Tolerancias', 'Simbología electrónica',
                         'Lectura de planos'],
            'actividades': 'Identificar resistencias, interpretar diagramas, construir circuito desde esquema',
            'materiales': 'Resistencias variadas, esquemas impresos, protoboard'
        },

        # Módulo 2
        {
            'titulo': 'Diodos - Parte 1',
            'objetivos': ['Entender funcionamiento del diodo', 'Conocer aplicaciones básicas'],
            'contenido': ['Estructura del diodo', 'Curva característica', 'Diodo en DC',
                         'Caída de voltaje directa'],
            'actividades': 'Probar diodo con multímetro, construir circuito con diodo LED',
            'materiales': 'Diodos 1N4007, LEDs, multímetro, protoboard'
        },
        {
            'titulo': 'Diodos - Parte 2: Rectificación',
            'objetivos': ['Entender rectificación', 'Construir rectificador'],
            'contenido': ['Rectificación media onda', 'Rectificación onda completa', 'Puente de diodos'],
            'actividades': 'Construir rectificador de media onda y puente, observar con LED',
            'materiales': 'Transformador pequeño, diodos, LEDs, capacitores'
        },
        {
            'titulo': 'Capacitores',
            'objetivos': ['Entender capacitancia', 'Aplicaciones de capacitores'],
            'contenido': ['Principio de funcionamiento', 'Tipos de capacitores', 'Carga y descarga',
                         'Capacitores en serie/paralelo'],
            'actividades': 'Experimentar con carga/descarga de capacitor, medir tiempo',
            'materiales': 'Capacitores electrolíticos y cerámicos, resistencias, LED, multímetro'
        },
        {
            'titulo': 'Filtros Capacitivos',
            'objetivos': ['Construir fuente DC filtrada', 'Entender filtrado'],
            'contenido': ['Rizado', 'Filtro capacitivo', 'Cálculo de capacitor de filtro'],
            'actividades': 'Agregar capacitor a rectificador, medir diferencia',
            'materiales': 'Rectificador del sesión anterior, capacitores grandes, osciloscopio (demo)'
        },
        {
            'titulo': 'Introducción a Transistores',
            'objetivos': ['Entender transistor BJT', 'Usar transistor como switch'],
            'contenido': ['Estructura del transistor', 'Terminales (B, C, E)', 'Transistor como switch',
                         'Hoja de datos básica'],
            'actividades': 'Construir circuito de transistor como switch controlando LED',
            'materiales': 'Transistores 2N2222 o BC547, resistencias, LEDs, protoboard'
        },
        {
            'titulo': 'Transistor como Amplificador',
            'objetivos': ['Entender amplificación básica', 'Calcular ganancia'],
            'contenido': ['Polarización del transistor', 'Ganancia de corriente (hFE)',
                         'Configuración emisor común', 'Punto de operación'],
            'actividades': 'Construir amplificador simple, medir entrada/salida',
            'materiales': 'Transistores, resistencias, potenciómetro, multímetro'
        },

        # Módulo 3
        {
            'titulo': 'Reguladores de Voltaje',
            'objetivos': ['Entender regulación de voltaje', 'Usar reguladores integrados'],
            'contenido': ['Necesidad de regulación', '7805 y familia 78XX', 'Reguladores LDO',
                         'Cálculo de disipadores'],
            'actividades': 'Construir fuente regulada +5V con 7805',
            'materiales': 'Regulador 7805, capacitores, transformador, puente de diodos'
        },
        {
            'titulo': 'Fuente de Alimentación Completa',
            'objetivos': ['Integrar todos los elementos', 'Construir fuente variable'],
            'contenido': ['Transformador', 'Rectificación', 'Filtrado', 'Regulación', 'Protecciones'],
            'actividades': 'Construir fuente DC regulada completa',
            'materiales': 'Todos los componentes anteriores, gabinete, conectores'
        },
        {
            'titulo': 'Potenciómetros y Controles',
            'objetivos': ['Trabajar con resistencias variables', 'Crear controles ajustables'],
            'contenido': ['Tipos de potenciómetros', 'Curva lineal vs logarítmica',
                         'Trimmers', 'Aplicaciones'],
            'actividades': 'Construir control de brillo LED, control de velocidad motor pequeño',
            'materiales': 'Potenciómetros variados, LEDs, motor DC pequeño, transistor'
        },
        {
            'titulo': 'Osciladores - El 555',
            'objetivos': ['Entender circuito integrado 555', 'Crear oscilador astable'],
            'contenido': ['Principio del 555', 'Modo astable', 'Cálculo de frecuencia',
                         'Aplicaciones comunes'],
            'actividades': 'Construir LED intermitente con 555, experimentar con frecuencias',
            'materiales': 'CI 555, resistencias, capacitores, LEDs, protoboard'
        },
        {
            'titulo': 'Timer y Monoestable',
            'objetivos': ['Usar 555 como timer', 'Crear retardos'],
            'contenido': ['Modo monoestable', 'Cálculo del tiempo', 'Disparo del timer',
                         'Aplicaciones prácticas'],
            'actividades': 'Construir timer que apaga LED después de cierto tiempo',
            'materiales': 'CI 555, componentes pasivos, switch, LED'
        },
        {
            'titulo': 'Amplificadores Operacionales - Intro',
            'objetivos': ['Conocer op-amp básico', 'Configuraciones simples'],
            'contenido': ['Símbolo y terminales', 'Alimentación dual', 'Comparador',
                         'Seguidor de voltaje'],
            'actividades': 'Construir comparador simple que enciende LED según voltaje',
            'materiales': 'Op-amp LM358 o TL082, resistencias, potenciómetro, LEDs'
        },

        # Módulo 4
        {
            'titulo': 'Electrónica Digital - Compuertas Lógicas',
            'objetivos': ['Entender lógica binaria', 'Trabajar con compuertas'],
            'contenido': ['Sistema binario', 'Compuertas AND, OR, NOT', 'Tablas de verdad',
                         'CIs digitales'],
            'actividades': 'Experimentar con compuertas 7408 (AND), 7432 (OR), 7404 (NOT)',
            'materiales': 'CIs digitales serie 74, LEDs, switches, resistencias'
        },
        {
            'titulo': 'Circuitos Lógicos Combinacionales',
            'objetivos': ['Diseñar circuitos lógicos', 'Implementar funciones booleanas'],
            'contenido': ['Álgebra booleana básica', 'Simplificación', 'Mapas de Karnaugh (intro)',
                         'Implementación'],
            'actividades': 'Diseñar e implementar circuito lógico para problema dado',
            'materiales': 'Compuertas variadas, protoboard, switches, LEDs'
        },
        {
            'titulo': 'Flip-Flops y Memoria',
            'objetivos': ['Entender elementos de memoria', 'Construir flip-flop básico'],
            'contenido': ['Concepto de memoria', 'Latch SR', 'Flip-flop D', 'Aplicaciones'],
            'actividades': 'Construir latch con compuertas NAND, probar funcionamiento',
            'materiales': 'Compuertas NAND (7400), switches, LEDs'
        },
        {
            'titulo': 'Contadores Digitales',
            'objetivos': ['Trabajar con contadores', 'Crear secuencias'],
            'contenido': ['Contadores binarios', 'CI 7490 (contador década)', 'Display de 7 segmentos',
                         'Decodificador 7447'],
            'actividades': 'Construir contador de 0-9 con display',
            'materiales': 'CI 7490, 7447, display 7 segmentos, resistencias'
        },
        {
            'titulo': 'Sensores y Actuadores',
            'objetivos': ['Interfaz con sensores', 'Controlar actuadores'],
            'contenido': ['LDR y fotodetectores', 'Termistores', 'Relés', 'Control de cargas'],
            'actividades': 'Construir circuito activado por luz (lámpara automática)',
            'materiales': 'LDR, transistor, relé, resistencias, lámpara pequeña'
        },
        {
            'titulo': 'Planificación Proyecto Final',
            'objetivos': ['Definir proyecto', 'Calcular componentes', 'Crear esquema'],
            'contenido': ['Ideas de proyectos', 'Esquema circuital', 'Lista de materiales',
                         'Plan de construcción'],
            'actividades': 'Cada estudiante diseña su proyecto con esquema y cálculos',
            'materiales': 'Papel, calculadora, catálogo de componentes'
        },
        {
            'titulo': 'Construcción Proyecto Final - Día 1',
            'objetivos': ['Iniciar construcción', 'Ensamblar componentes principales'],
            'contenido': ['Verificación de componentes', 'Ensamblaje paso a paso', 'Pruebas parciales'],
            'actividades': 'Construcción supervisada del proyecto',
            'materiales': 'Componentes según proyecto individual'
        },
        {
            'titulo': 'Construcción Proyecto Final - Día 2 y Presentación',
            'objetivos': ['Finalizar proyecto', 'Documentar', 'Presentar'],
            'contenido': ['Pruebas finales', 'Ajustes', 'Documentación', 'Presentación oral'],
            'actividades': 'Completar y presentar proyecto, explicación técnica a compañeros',
            'materiales': 'Componentes finales, documentación, cámara para fotos'
        }
    ],

    'evaluacion': {
        'descripcion': '''
        Evaluación basada en comprensión teórica, habilidad práctica y capacidad de diseño.
        Se valora el proceso de pensamiento crítico, resolución de problemas y calidad
        de construcción.
        ''',
        'criterios': {
            'Tareas y ejercicios teóricos': '20%',
            'Prácticas de laboratorio (circuitos construidos)': '30%',
            'Participación y trabajo en clase': '15%',
            'Proyecto final (diseño, construcción y presentación)': '35%'
        }
    },

    'proyecto_final': {
        'titulo': 'Proyecto Electrónico Aplicado',
        'descripcion': '''
        Diseño y construcción de un circuito electrónico funcional que resuelva un problema
        real o implemente una función específica. Ejemplos: fuente de alimentación variable,
        cargador de baterías, control de temperatura, sistema de alarma, timer programable,
        amplificador de audio, etc.
        ''',
        'entregables': [
            'Esquema circuital completo y cálculos',
            'Circuito funcional construido y probado',
            'Documentación técnica (componentes, funcionamiento)',
            'Presentación oral de 5 minutos explicando diseño y operación',
            'Demostración práctica del funcionamiento'
        ]
    },

    'materiales': [
        {'cantidad': 1, 'nombre': 'Protoboard 830 puntos', 'descripcion': 'Tableta de prototipado grande',
         'precio_unitario': 120.00},
        {'cantidad': 1, 'nombre': 'Multímetro digital', 'descripcion': 'Multímetro básico',
         'precio_unitario': 250.00},
        {'cantidad': 1, 'nombre': 'Kit de componentes pasivos', 'descripcion': 'Resistencias, capacitores, inductores',
         'precio_unitario': 180.00},
        {'cantidad': 1, 'nombre': 'Kit de diodos', 'descripcion': '1N4007, LEDs, Zener',
         'precio_unitario': 100.00},
        {'cantidad': 10, 'nombre': 'Transistores variados', 'descripcion': '2N2222, BC547, TIP41',
         'precio_unitario': 8.00},
        {'cantidad': 1, 'nombre': 'Kit de CIs', 'descripcion': '555, 7805, LM358, 74XX',
         'precio_unitario': 200.00},
        {'cantidad': 1, 'nombre': 'Cables jumper (pack)', 'descripcion': '65 cables variados',
         'precio_unitario': 80.00},
        {'cantidad': 3, 'nombre': 'Potenciómetros', 'descripcion': '10k, 100k, 1M',
         'precio_unitario': 12.00},
        {'cantidad': 1, 'nombre': 'Switches y botones', 'descripcion': 'Variados',
         'precio_unitario': 60.00},
        {'cantidad': 1, 'nombre': 'Fuente de alimentación', 'descripcion': 'Ajustable 0-12V, 2A',
         'precio_unitario': 280.00},
        {'cantidad': 5, 'nombre': 'Baterías 9V', 'descripcion': 'Con conectores',
         'precio_unitario': 35.00},
        {'cantidad': 1, 'nombre': 'Display 7 segmentos', 'descripcion': 'Cátodo común',
         'precio_unitario': 25.00},
        {'cantidad': 1, 'nombre': 'Kit de sensores', 'descripcion': 'LDR, termistor, etc',
         'precio_unitario': 150.00},
        {'cantidad': 2, 'nombre': 'Relés 5V', 'descripcion': 'Relé SPDT',
         'precio_unitario': 25.00}
    ]
}


# ============================================================================
# CURSO DE ELECTRÓNICA - 15+ AÑOS
# ============================================================================

electronica_15_mas = {
    'nombre': 'Curso de Electrónica Avanzada',
    'grupo_edad': '15+ años',
    'duracion_sesion': '1.5 horas',
    'nivel': 'Intermedio-Avanzado',
    'precio_curso': 3800.00,
    'costo_materiales': 1850.00,
    'ruta': 'cursos/01-Electronica/15-mas-años',

    'descripcion': '''
    Curso intensivo de electrónica que abarca desde fundamentos sólidos hasta aplicaciones
    avanzadas. Incluye análisis profundo de circuitos analógicos y digitales, diseño con
    amplificadores operacionales, fuentes de alimentación conmutadas, introducción a RF,
    y uso de herramientas profesionales como simuladores y osciloscopio. Ideal para adultos
    que buscan una formación técnica seria o base para ingeniería.
    ''',

    'objetivos': [
        'Dominar análisis de circuitos AC y DC',
        'Diseñar circuitos analógicos con componentes discretos e integrados',
        'Trabajar con electrónica de potencia básica',
        'Comprender y aplicar transformada de Fourier en análisis de señales',
        'Usar herramientas profesionales (osciloscopio, generador de funciones, simuladores)',
        'Diseñar PCBs básicos',
        'Introducción a microcontroladores y sistemas embebidos',
        'Desarrollar proyectos complejos con documentación profesional'
    ],

    'requisitos': [
        'Matemáticas nivel preparatoria (álgebra, trigonometría)',
        'Conocimientos básicos de física (electricidad recomendable)',
        'Compromiso para estudio teórico y práctico',
        'Laptop personal (para simulaciones y diseño)'
    ],

    'modulos': [
        {
            'nombre': 'Análisis de Circuitos Avanzado',
            'sesiones': '1-6',
            'descripcion': 'Teoremas de circuitos, análisis AC, impedancias y resonancia',
            'contenido_detallado': [
                {
                    'titulo': 'Técnicas avanzadas',
                    'puntos': ['Teoremas de Thévenin y Norton', 'Superposición',
                              'Análisis de mallas y nodos', 'Circuitos AC']
                }
            ]
        },
        {
            'nombre': 'Semiconductores y Amplificación',
            'sesiones': '7-12',
            'descripcion': 'Diodos, transistores BJT y MOSFET, amplificadores multietapa',
            'contenido_detallado': [
                {
                    'titulo': 'Dispositivos activos',
                    'puntos': ['Características de semiconductores', 'Amplificadores clase A/B',
                              'MOSFET como switch', 'Diseño de amplificadores']
                }
            ]
        },
        {
            'nombre': 'Circuitos Integrados y Aplicaciones',
            'sesiones': '13-18',
            'descripcion': 'Op-amps, comparadores, osciladores, PLLs, conversores ADC/DAC',
            'contenido_detallado': [
                {
                    'titulo': 'Sistemas integrados',
                    'puntos': ['Amplificadores operacionales avanzados', 'Filtros activos',
                              'Conversión analógica-digital', 'Generadores de señal']
                }
            ]
        },
        {
            'nombre': 'Sistemas Digitales y Proyecto Final',
            'sesiones': '19-24',
            'descripcion': 'Lógica secuencial, memorias, intro a MCU y proyecto complejo',
            'contenido_detallado': [
                {
                    'titulo': 'Digital avanzado',
                    'puntos': ['Máquinas de estados', 'Microcontroladores básicos',
                              'Comunicación serial', 'Integración de sistemas']
                }
            ]
        }
    ],

    'sesiones': [
        # Módulo 1
        {
            'titulo': 'Repaso de Fundamentos y Teoremas Básicos',
            'objetivos': ['Repasar leyes fundamentales', 'Aplicar teoremas de circuitos'],
            'contenido': ['Leyes de Ohm y Kirchhoff', 'Teorema de Thévenin', 'Teorema de Norton',
                         'Equivalentes de circuitos'],
            'actividades': 'Resolver circuitos complejos usando teoremas, verificar en simulador',
            'materiales': 'Laptop con simulador (LTspice o similar), calculadora'
        },
        {
            'titulo': 'Análisis de Mallas y Nodos',
            'objetivos': ['Dominar método de mallas', 'Dominar método de nodos'],
            'contenido': ['Análisis de mallas', 'Análisis de nodos', 'Sistemas de ecuaciones',
                         'Matrices (intro)'],
            'actividades': 'Resolver circuitos multipuerto, comparar métodos',
            'materiales': 'Problemas impresos, calculadora, simulador'
        },
        {
            'titulo': 'Introducción a Circuitos AC',
            'objetivos': ['Entender señales sinusoidales', 'Calcular valores RMS'],
            'contenido': ['Señales AC', 'Frecuencia y periodo', 'Valor pico y RMS', 'Fase'],
            'actividades': 'Medir señales AC con osciloscopio, calcular parámetros',
            'materiales': 'Osciloscopio, generador de funciones, multímetro'
        },
        {
            'titulo': 'Impedancia y Fasores',
            'objetivos': ['Trabajar con números complejos', 'Calcular impedancias'],
            'contenido': ['Impedancia capacitiva', 'Impedancia inductiva', 'Notación fasorial',
                         'Cálculos AC con fasores'],
            'actividades': 'Resolver circuitos AC usando fasores, verificar con mediciones',
            'materiales': 'Componentes RLC, generador, osciloscopio, calculadora'
        },
        {
            'titulo': 'Resonancia en Circuitos RLC',
            'objetivos': ['Entender resonancia serie y paralelo', 'Calcular frecuencia de resonancia'],
            'contenido': ['Circuito RLC serie', 'Circuito RLC paralelo', 'Factor Q',
                         'Ancho de banda'],
            'actividades': 'Construir circuito resonante, medir respuesta en frecuencia',
            'materiales': 'Inductores, capacitores, resistencias, generador de funciones, osciloscopio'
        },
        {
            'titulo': 'Filtros Pasivos',
            'objetivos': ['Diseñar filtros RC y RLC', 'Analizar respuesta en frecuencia'],
            'contenido': ['Filtros pasa-bajas', 'Filtros pasa-altas', 'Filtros pasa-banda',
                         'Diagrama de Bode'],
            'actividades': 'Diseñar y construir filtros, graficar respuesta',
            'materiales': 'Componentes RLC, generador, osciloscopio, software para Bode'
        },

        # Módulo 2
        {
            'titulo': 'Semiconductores: Diodos Avanzados',
            'objetivos': ['Profundizar en física de semiconductores', 'Diodos especiales'],
            'contenido': ['Juntura PN', 'Diodos Zener', 'Diodos Schottky', 'Varactores', 'LEDs de potencia'],
            'actividades': 'Caracterizar diodos, construir regulador Zener, probar LEDs de potencia',
            'materiales': 'Diodos variados, trazador de curvas (o simulación), resistencias'
        },
        {
            'titulo': 'Transistor BJT: Análisis Profundo',
            'objetivos': ['Analizar punto de operación', 'Diseñar polarización estable'],
            'contenido': ['Regiones de operación', 'Recta de carga', 'Polarización por divisor',
                         'Estabilidad térmica'],
            'actividades': 'Diseñar y calcular circuito de polarización, medir punto Q',
            'materiales': 'Transistores BJT, resistencias, multímetro, osciloscopio'
        },
        {
            'titulo': 'Amplificador Emisor Común',
            'objetivos': ['Diseñar amplificador de pequeña señal', 'Calcular ganancia'],
            'contenido': ['Configuración EC', 'Modelo de pequeña señal', 'Ganancia de voltaje',
                         'Impedancias de entrada/salida'],
            'actividades': 'Diseñar amplificador, medir ganancia con osciloscopio',
            'materiales': 'Transistores, resistencias, capacitores, generador, osciloscopio'
        },
        {
            'titulo': 'Configuraciones CC y BC',
            'objetivos': ['Entender seguidor de emisor', 'Conocer base común'],
            'contenido': ['Colector común (seguidor)', 'Base común', 'Comparación de configuraciones',
                         'Aplicaciones específicas'],
            'actividades': 'Construir seguidor de emisor, medir impedancias',
            'materiales': 'Transistores, componentes pasivos, instrumentos de medición'
        },
        {
            'titulo': 'MOSFET: Fundamentos',
            'objetivos': ['Entender MOSFET', 'Comparar con BJT'],
            'contenido': ['Estructura del MOSFET', 'MOSFET canal N y P', 'Regiones de operación',
                         'MOSFET como switch'],
            'actividades': 'Usar MOSFET para conmutar cargas, comparar con BJT',
            'materiales': 'MOSFETs (IRFZ44, 2N7000), resistencias, cargas (motor, lámpara)'
        },
        {
            'titulo': 'Amplificador de Potencia',
            'objetivos': ['Diseñar amplificador clase A/B', 'Gestionar disipación'],
            'contenido': ['Clases de amplificadores', 'Push-pull', 'Distorsión de cruce',
                         'Disipadores'],
            'actividades': 'Construir amplificador simple de audio, medir potencia',
            'materiales': 'Transistores de potencia, disipadores, altavoz, generador de audio'
        },

        # Módulo 3
        {
            'titulo': 'Amplificadores Operacionales: Fundamentos',
            'objetivos': ['Entender modelo ideal de op-amp', 'Configuraciones básicas'],
            'contenido': ['Características del op-amp ideal', 'Retroalimentación negativa',
                         'Inversor y no-inversor', 'Sumador'],
            'actividades': 'Construir inversores y no-inversores, verificar ganancias',
            'materiales': 'Op-amps (LM358, TL071), resistencias, generador, osciloscopio'
        },
        {
            'titulo': 'Aplicaciones de Op-Amps',
            'objetivos': ['Diseñar circuitos prácticos con op-amps', 'Integrador y derivador'],
            'contenido': ['Integrador', 'Derivador', 'Convertidor I-V y V-I', 'Rectificador de precisión'],
            'actividades': 'Implementar integrador y derivador, observar señales',
            'materiales': 'Op-amps, capacitores, resistencias, generador, osciloscopio'
        },
        {
            'titulo': 'Comparadores y Schmitt Trigger',
            'objetivos': ['Diseñar comparadores', 'Implementar histéresis'],
            'contenido': ['Comparador simple', 'Comparador de ventana', 'Schmitt trigger',
                         'Aplicaciones con histéresis'],
            'actividades': 'Construir Schmitt trigger, probar con señal ruidosa',
            'materiales': 'Op-amps o comparadores (LM311), resistencias, LEDs'
        },
        {
            'titulo': 'Filtros Activos',
            'objetivos': ['Diseñar filtros activos', 'Comparar con pasivos'],
            'contenido': ['Filtros Sallen-Key', 'Filtros pasa-bajas activos', 'Filtros pasa-altas activos',
                         'Filtros de orden superior'],
            'actividades': 'Diseñar e implementar filtro activo de 2º orden, medir respuesta',
            'materiales': 'Op-amps, resistencias, capacitores, generador, osciloscopio'
        },
        {
            'titulo': 'Osciladores con Op-Amps',
            'objetivos': ['Generar señales con osciladores', 'Diseñar oscilador de Wien'],
            'contenido': ['Condición de oscilación', 'Oscilador de puente de Wien',
                         'Oscilador de fase', 'Control de amplitud'],
            'actividades': 'Construir oscilador de Wien, medir frecuencia y estabilidad',
            'materiales': 'Op-amps, resistencias, capacitores, lámpara incandescente (opcional)'
        },
        {
            'titulo': 'Conversión ADC y DAC',
            'objetivos': ['Entender conversión A/D y D/A', 'Usar conversores integrados'],
            'contenido': ['Principios de conversión', 'DAC R-2R', 'ADC por aproximaciones sucesivas',
                         'Resolución y muestreo'],
            'actividades': 'Experimentar con DAC y ADC básicos, teorema de Nyquist',
            'materiales': 'CIs ADC0804 y DAC0808, resistencias de precisión, componentes'
        },

        # Módulo 4
        {
            'titulo': 'Lógica Secuencial: Flip-Flops',
            'objetivos': ['Dominar elementos de memoria', 'Diseñar con flip-flops'],
            'contenido': ['FF tipo D, JK, T', 'Tablas de excitación', 'Registros de desplazamiento',
                         'Aplicaciones'],
            'actividades': 'Construir circuitos con FFs 7474, crear registro de desplazamiento',
            'materiales': 'CIs 7474, 7476, switches, LEDs, generador de pulsos'
        },
        {
            'titulo': 'Contadores y Divisores de Frecuencia',
            'objetivos': ['Diseñar contadores', 'Implementar divisores'],
            'contenido': ['Contadores asíncronos', 'Contadores síncronos', 'Contadores módulo N',
                         'Aplicaciones en relojería'],
            'actividades': 'Diseñar contador módulo 10, crear divisor de frecuencia',
            'materiales': 'FFs, compuertas lógicas, displays, generador'
        },
        {
            'titulo': 'Memorias Digitales',
            'objetivos': ['Entender arquitectura de memorias', 'Usar memorias simples'],
            'contenido': ['RAM vs ROM', 'Direccionamiento', 'Buses de datos', 'Memorias EEPROM'],
            'actividades': 'Experimentar con memoria EEPROM simple, programación básica',
            'materiales': 'EEPROM 24C02, microcontrolador (programador), resistencias pull-up'
        },
        {
            'titulo': 'Introducción a Microcontroladores',
            'objetivos': ['Conocer arquitectura básica de MCU', 'Programación simple'],
            'contenido': ['Arquitectura de MCU', 'Periféricos', 'GPIO', 'Programación en C básica'],
            'actividades': 'Programar MCU simple (ATtiny o similar) para parpadear LED',
            'materiales': 'Microcontrolador, programador, LEDs, protoboard'
        },
        {
            'titulo': 'Comunicación Serial',
            'objetivos': ['Entender UART, SPI, I2C', 'Implementar comunicación'],
            'contenido': ['UART/USART', 'SPI', 'I2C', 'Protocolos y timing'],
            'actividades': 'Comunicar MCU con PC vía UART, enviar datos de sensor',
            'materiales': 'MCU con UART, cable USB-serial, sensor I2C (opcional)'
        },
        {
            'titulo': 'Proyecto Final: Definición y Diseño',
            'objetivos': ['Definir proyecto complejo', 'Crear esquemático completo'],
            'contenido': ['Especificaciones del proyecto', 'Diseño modular', 'Esquemático profesional',
                         'Lista de materiales (BOM)'],
            'actividades': 'Cada estudiante define y diseña proyecto, crear esquema en software',
            'materiales': 'Laptop, software de diseño (KiCad, Eagle), documentación'
        },
        {
            'titulo': 'Construcción Proyecto Final - Parte 1',
            'objetivos': ['Iniciar construcción', 'Ensamblar etapas principales'],
            'contenido': ['Ensamblaje por bloques', 'Pruebas incrementales', 'Debugging'],
            'actividades': 'Construcción supervisada, pruebas de cada etapa',
            'materiales': 'Componentes según proyecto, instrumentos de medición'
        },
        {
            'titulo': 'Construcción Proyecto Final - Parte 2 y Presentación',
            'objetivos': ['Completar proyecto', 'Documentar profesionalmente', 'Presentar'],
            'contenido': ['Integración final', 'Calibración', 'Documentación técnica',
                         'Presentación profesional'],
            'actividades': 'Finalizar proyecto, crear documento técnico, presentación de 10 minutos',
            'materiales': 'Componentes finales, laptop para documentación'
        }
    ],

    'evaluacion': {
        'descripcion': '''
        Evaluación rigurosa que combina teoría profunda, habilidad práctica de construcción,
        capacidad de análisis y diseño, y calidad de documentación. Se espera nivel de
        ingeniería en el proyecto final.
        ''',
        'criterios': {
            'Exámenes teóricos (parciales)': '25%',
            'Prácticas de laboratorio y reportes': '25%',
            'Tareas y simulaciones': '15%',
            'Proyecto final (diseño, construcción, documentación y presentación)': '35%'
        }
    },

    'proyecto_final': {
        'titulo': 'Proyecto de Ingeniería Electrónica',
        'descripcion': '''
        Diseño y construcción de un sistema electrónico complejo que integre múltiples conceptos
        del curso. Debe incluir etapas analógicas y digitales, y resolver un problema real o
        implementar una funcionalidad avanzada. Ejemplos: fuente conmutada, sistema de adquisición
        de datos, controlador PID analógico, sistema de comunicación, analizador de espectro simple,
        sintetizador de audio, etc.
        ''',
        'entregables': [
            'Documento técnico completo (análisis, cálculos, diseño)',
            'Esquemático profesional (software CAD)',
            'Lista de materiales (BOM) con justificación',
            'Circuito funcional construido y probado exhaustivamente',
            'Resultados de pruebas y mediciones (gráficas, tablas)',
            'Código fuente (si aplica MCU)',
            'Presentación técnica de 10-15 minutos',
            'Demostración en vivo del funcionamiento'
        ]
    },

    'materiales': [
        {'cantidad': 1, 'nombre': 'Protoboard grande (1680 puntos)', 'descripcion': 'Tableta profesional',
         'precio_unitario': 180.00},
        {'cantidad': 1, 'nombre': 'Multímetro digital profesional', 'descripcion': 'True RMS, capacitancia',
         'precio_unitario': 450.00},
        {'cantidad': 1, 'nombre': 'Kit de componentes premium', 'descripcion': 'Resistencias 1%, capacitores precisión',
         'precio_unitario': 280.00},
        {'cantidad': 1, 'nombre': 'Kit de semiconductores', 'descripcion': 'Diodos, transistores, MOSFETs variados',
         'precio_unitario': 250.00},
        {'cantidad': 1, 'nombre': 'Kit de CIs variados', 'descripcion': 'Op-amps, 555, reguladores, lógica 74XX',
         'precio_unitario': 320.00},
        {'cantidad': 1, 'nombre': 'Microcontrolador con programador', 'descripcion': 'ATmega328P o similar + programador',
         'precio_unitario': 280.00},
        {'cantidad': 1, 'nombre': 'Cables jumper premium (set)', 'descripcion': '120 cables diversos',
         'precio_unitario': 120.00},
        {'cantidad': 1, 'nombre': 'Potenciómetros de precisión (set)', 'descripcion': 'Multi-vuelta y estándar',
         'precio_unitario': 80.00},
        {'cantidad': 1, 'nombre': 'Fuente de alimentación dual', 'descripcion': '±12V, 2A ajustable',
         'precio_unitario': 380.00},
        {'cantidad': 1, 'nombre': 'Generador de funciones', 'descripcion': 'Hasta 2MHz, varias formas de onda',
         'precio_unitario': 850.00},
        {'cantidad': 1, 'nombre': 'Kit de inductores y transformadores', 'descripcion': 'Varios valores',
         'precio_unitario': 150.00},
        {'cantidad': 1, 'nombre': 'Kit de displays y componentes digitales', 'descripcion': '7-seg, matrices LED',
         'precio_unitario': 120.00},
        {'cantidad': 1, 'nombre': 'Kit de sensores diversos', 'descripcion': 'Temperatura, luz, corriente',
         'precio_unitario': 180.00},
        {'cantidad': 1, 'nombre': 'Componentes para proyecto final', 'descripcion': 'Presupuesto para proyecto',
         'precio_unitario': 300.00}
    ]
}


# ============================================================================
# GENERAR TODOS LOS CURSOS
# ============================================================================

def generar_todos():
    print("=" * 70)
    print("GENERANDO CURSOS DE ELECTRÓNICA")
    print("=" * 70)
    print()

    # Curso 9-13 años
    generador_1 = GeneradorCurso(electronica_9_13)
    generador_1.generar_todo()

    # Curso 14-18 años
    generador_2 = GeneradorCurso(electronica_14_18)
    generador_2.generar_todo()

    # Curso 15+ años
    generador_3 = GeneradorCurso(electronica_15_mas)
    generador_3.generar_todo()

    print("=" * 70)
    print("✓ TODOS LOS CURSOS DE ELECTRÓNICA GENERADOS EXITOSAMENTE")
    print("=" * 70)


if __name__ == "__main__":
    generar_todos()
