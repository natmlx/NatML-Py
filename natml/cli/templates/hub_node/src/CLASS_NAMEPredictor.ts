/* 
*   NAME
*   Copyright (c) 2022 AUTHOR.
*/

import { MLModel, MLHubModel, IMLAsyncPredictor, MLFeature } from "natml"

/**
 * DESCRIPTION
 */
export class CLASS_NAMEPredictor implements IMLAsyncPredictor<object> {

    private readonly model: MLHubModel;

    /**
     * Create the predictor.
     * @param model ML model.
     */
    public constructor (model: MLModel) {
        this.model = model as MLHubModel;
    }

    /**
     * Make a prediction.
     * @param features Input features.
     * @returns Prediction output.
     */
    public async predict (...inputs: MLFeature[]) {
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
        return null as object;
    }
}