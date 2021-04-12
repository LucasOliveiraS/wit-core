greet = {
    "text":"Hello, good morning",
    "intents":[
        {
            "id":"226449025939731",
            "name":"greet",
            "confidence":0.9954
        }
    ],
    "entities":{
        
    },
    "traits":{
        
    }
}

temperature_get = {
    "text":"What is the weather like in S\u00e3o Paulo",
    "intents":[
        {
            "id":"235367071262382",
            "name":"temperature_get",
            "confidence":0.9982
        }
    ],
    "entities":{
        "city:city":[
            {
                "id":"307760787416690",
                "name":"city",
                "role":"city",
                "start":28,
                "end":37,
                "body":"S\u00e3o Paulo",
                "confidence":0.9482,
                "entities":[
                    
                ],
                "value":"S\u00e3o Paulo",
                "type":"value"
            }
        ]
    },
    "traits":{
        
    }
}

temperature_set = {
    "text":"turn the temperature to 62 degrees",
    "intents":[
        {
            "id":"240369317812131",
            "name":"temperature_set",
            "confidence":0.996
        }
    ],
    "entities":{
        "wit$temperature:temperature":[
            {
                "id":"305684514486650",
                "name":"wit$temperature",
                "role":"temperature",
                "start":24,
                "end":34,
                "body":"62 degrees",
                "confidence":0.971,
                "entities":[
                    
                ],
                "unit":"degree",
                "type":"value",
                "value":62
            }
        ]
    },
    "traits":{
        
    }
}