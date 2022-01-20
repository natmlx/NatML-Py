# NAME
DESCRIPTION

## Making Predictions
First, create the predictor:
```typescript
// Fetch the model data from NatML Hub
const modelData = await MLModelData.fromHub("TAG");
// Deserialize the model
const model = modelData.deserialize();
// Create the predictor
const predictor = new CLASS_NAMEPredictor(model);
```

Then create an input feature:
```typescript
/**
 * Illustrate how to create an input feature.
 * Make sure to show how to set required parameters, e.g. normalization on images
 */
```

Finally, make predictions:
```typescript
// Make a prediction
const result = await predictor.predict(input);
```

## Requirements
- [NatML 0.0.4+](https://www.npmjs.com/package/natml)