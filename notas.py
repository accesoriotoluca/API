"""
^ monitoreo endpoints api
~ disponibilidad:
verificar continuamente endpoints están disponibles, responden correctamente, herramientas de monitoreo si no está disponible o devuelve código d error, genera alerta para notificar
~ tiempo de respuesta:
medir tiempo d respuesta, establecer umbrales d tiempo d respuesta aceptables y generar alertas si tiempos respuesta superan esos umbrales.
~ rendimiento:
métricas de rendimiento: uso de recursos (CPU, memoria, ancho de banda), capacidad de manejar cargas d trabajo altas, identificar cuellos de botella, problemas de escalabilidad o limitaciones de recursos
~ errores:
monitorear registrar errores identificar problemas recurrentes inusuales. herramientas de monitoreo de registros para capturar analizar los registros generados por los endpoints
~ seguridad:
detectar intentos de acceso no autorizados, soluciones para monitorean el tráfico, detectan patrones sospechosos y bloquean o notifican sobre actividades maliciosas
~ cambios:
cambios en endpoints, monitorear su impacto. verificar si las solicitudes y respuestas siguen siendo compatibles, problemas de compatibilidad o degradación del rendimiento. pruebas de regresión automatizadas y monitorear las métricas relevantes para asegurarse de que cambios no introduzcan problemas inesperados

! endpoints están directamente relacionados con las URL
endpoints son las rutas que se envían solicitudes para realizar operaciones o acceder a recursos
Cada endpont representa una funcionalidad o recurso específico 
^ parámetros '&' parámetros '=' valor 
se denominan "parámetros de consulta" o "parámetros de URL"
mayoría d casos, no es importante el orden d los parámetros
El servidor de la API debería poder interpretar y procesarlos

^ "Schema Definitions"
describen estructura, formato de datos qc envían o reciben
define tipos de datos permitidos, propiedades, restricciones y relaciones entre datos
suelen seguir formato específico, JSON Schema o GraphQL Schema
contrato o acuerdo entre clientes y servidor
~ Validación de datos:
asegura cumplan estructura, restricciones especificadas. mantener integridad coherencia de datos
~ Generación de documentación:
generardo automáticamente, descripciones de los campos, tipos de datos esperados, reglas de validación y ejemplos
~ Generación de código:
es posible generar automáticamente código del lado del cliente o del servidor. acelera proceso d desarrollo y reduce la posibilidad de errores en implementación
~Flexibilidad y evolución:
definiciones de esquemas permiten realizar cambios de manera controlada y predecible. pueden ser versionados y gestionados de manera independiente, facilita la evolución de la API sin romper la compatibilidad

^ SDK
conjunto de herramientas, bibliotecas, documentación y ejemplos de código, compiladores, depuradores, emuladores, herramientas de prueba y más. que facilitan el desarrollo de aplicaciones para una plataforma específica. SDK está diseñado para trabajar con un sistema operativo, una plataforma de hardware o un entorno de desarrollo específico.

^ $ curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN'  https://api.mercadolibre.com/users/me
El signo "$" al inicio de una variable en la línea de comandos de Linux o Unix se utiliza para indicar que se trata de una variable de entorno. En el ejemplo que proporcionaste, "$ACCESS_TOKEN" es una variable de entorno que almacena un token de acceso.
Cuando se ejecuta el comando en la terminal, el sistema operativo reemplaza "$ACCESS_TOKEN" con el valor real almacenado en la variable de entorno antes de ejecutar la solicitud CURL. Por lo tanto, se debe quitar el signo "$" para que CURL interprete correctamente el valor de la variable de entorno y lo incluya en la solicitud 


"""