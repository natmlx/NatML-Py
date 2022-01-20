/* 
*   NAME
*   Copyright (c) 2022 AUTHOR.
*/

namespace CLASS_NAME {

    using System;
    using System.Linq;
    using NatSuite.ML;
    using NatSuite.ML.Extensions;
    using NatSuite.ML.Features;
    using NatSuite.ML.Internal;
    using NatSuite.ML.Types;

    /// <summary>
    /// DESCRIPTION
    /// </summary>
    public sealed class CLASS_NAMEPredictor : IMLPredictor<object> {

        #region --Client API--
        /// <summary>
        /// Create the predictor.
        /// </summary>
        /// <param name="model">ML model.</param>
        public CLASS_NAMEPredictor (MLModel model) {
            this.model = model as MLEdgeModel;
        }

        /// <summary>
        /// Make a prediction.
        /// </summary>
        /// <param name="inputs">Input features.</param>
        /// <returns>Prediction output.</returns>
        public unsafe object Predict (params MLFeature[] inputs) {
            // Check inputs
            /**
             * Check that the correct number of inputs is passed in.
             * Also check that the inputs have the correct types (array/image/audio).
             */
            // Predict
            /**
             * Create native input feature(s) from the input(s).
             * Make a prediction with the model.
             * Release the native input feature(s).
             */
            // Marshal
            /**
             * Read the output feature data and create familiar return types.
             * Release the native output feature(s).
             */
            return default;
        }
        #endregion


        #region --Operations--
        private readonly MLEdgeModel model;

        void IDisposable.Dispose () { }
        #endregion
    }
}