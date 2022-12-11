# Modules:
 * external_data_handler (Moduł pobierania danych z zewnętrznych źródeł)
   * external_data_handler → data_storage 
 * data_storage (Moduł przechowywania danych)
   * data_storage ← external_data_handler
   * data_storage ← data_processing
 * data_processing (Moduł obróbki danych)
   * data_processing → data_storage
   * data_processing ← prediction_engine
   * data_processing ← rest_api
 * prediction_engine (Silnik predykcji)
   * prediction_engine → data_processing
 * rest_api (Moduł REST API)
   * rest_api → data_processing
   * rest_api → visualization
 * visualization (Moduł wizualizacji danych)
   * visualization → rest_api 
 * frontend (Moduł frontendu)
   * frontend → rest_api


Dependencies: 
  * dependent_module → module  =  means that the module is dependent on the module on the right
  * module ← dependent_module   =  means that the module is dependent on the module on the left 
