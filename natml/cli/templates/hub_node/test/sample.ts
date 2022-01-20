import { MLModelData, MLImageFeature } from "natml"
import { CLASS_NAMEPredictor } from "../src"

async function main () {
    // Fetch the model data from NatML Hub
    const modelData = await MLModelData.fromHub("TAG", process.env.ACCESS_KEY);
    // Deserialize the model
    const model = modelData.deserialize();
    // Create the predictor
    const predictor = new CLASS_NAMEPredictor(model);
    // Predict
    // ...
}

main();