# NAME
DESCRIPTION

## Making Predictions
First, create the predictor:
```csharp
// Fetch the model data from NatML Hub
var modelData = await MLModelData.FromHub("TAG");
// Deserialize the model
var model = modelData.Deserialize();
// Create the predictor
var predictor = new CLASS_NAMEPredictor(model);
```

Then create an input feature:
```csharp
/**
 * Illustrate how to create an input feature.
 * Make sure to show how to set required parameters, e.g. normalization on images
 */
```

Finally, make predictions:
```csharp
// Make a prediction
var prediction = predictor.Predict(input);
```

## Requirements
- Unity 2019.2+
- NatML 1.0+