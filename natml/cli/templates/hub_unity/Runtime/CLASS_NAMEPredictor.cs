/* 
*   NAME
*   Copyright (c) 2022 AUTHOR.
*/

namespace CLASS_NAME {

    using System;
    using System.Linq;
    using System.Threading.Tasks;
    using NatSuite.ML;
    using NatSuite.ML.Extensions;
    using NatSuite.ML.Features;
    using NatSuite.ML.Internal;
    using NatSuite.ML.Types;

    /// <summary>
    /// DESCRIPTION
    /// </summary>
    public sealed class CLASS_NAMEPredictor : IMLAsyncPredictor<object> {

        #region --Client API--
        /// <summary>
        /// Create the predictor.
        /// </summary>
        /// <param name="model">ML model.</param>
        public CLASS_NAMEPredictor (MLModel model) {
            this.model = model as MLHubModel;
        }

        /// <summary>
        /// Make a prediction.
        /// </summary>
        /// <param name="inputs">Input features.</param>
        /// <returns>Prediction output.</returns>
        public async Task<object> Predict (params MLFeature[] inputs) {
            /**
             * __Check inputs__
             * Check that the correct number of inputs is passed in.
             * Also check that the inputs have the correct types (array/image/audio).
             */
            /**
             * __Predict__
             * Create Hub input feature(s) from the input(s).
             * Make a prediction with the Hub model.
             */
            /**
             * __Marshal__
             * Read the output feature data and create familiar return types.
             */
            return null;
        }
        #endregion


        #region --Operations--
        private readonly MLHubModel model;

        void IDisposable.Dispose () { }
        #endregion
    }
}