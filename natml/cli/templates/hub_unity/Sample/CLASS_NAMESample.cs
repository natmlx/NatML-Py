/* 
*   NAME
*   Copyright (c) 2022 AUTHOR.
*/

namespace CLASS_NAME.Examples {

    using UnityEngine;
    using NatSuite.ML;
    using NatSuite.ML.Features;

    public sealed class CLASS_NAMESample : MonoBehaviour {
        
        [Header(@"NatML Hub")]
        public string accessKey;

        async void Start () {
            Debug.Log("Fetching model from NatML Hub");
            // Fetch model data from NatML Hub // Get your access key from https://hub.natml.ai/profile
            var modelData = await MLModelData.FromHub("TAG", accessKey);
            // Deserialize the model
            var model = modelData.Deserialize();
            // Create the predictor
            var predictor = new CLASS_NAMEPredictor(model);

            // Make predictions
            // ...

            // Dispose the model
            model.Dispose();
        }
    }
}