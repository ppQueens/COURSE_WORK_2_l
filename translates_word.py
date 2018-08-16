fields = {"weight": "вес", "socket_type": "тип сокета", "cache 1": "кэш первого уровня", "cache 2": "кэш второго уровня",
          "cache 3": "кэш третьего уровня", "core":"число ядер","thread":"число потоков",
          "temperature":"максимальная температура","warranty":"гарантия","frequency":"внутренняя тактовая частота",
          "family":"cемейство","part_number":"модель", "TDP":"Мощность TDP","manufacturer":"производитель",
          "slot":"слот","formfactor":"формфактор","integratedvideo":"Интегрированная графика"}

values = {"false":"Нет","true":"Да"}

status = {"new":"новый","processed":"обработан","canceled":"отменен","sent":"отправлен покупателю",
          "need clarification":"требует уточнения","fulfilled":"выполнен"}
categories = {"материнские платы": "motherboards", "процессоры": "processors"}


reversed_categories = {v: k for k, v in categories.items()}

