import requests
import pandas as pd
import io
import sdmx



# ================================
# Function to Retrieve Available Dataflows
# ================================
def get_available_dataflows(client):
    """
    Fetch available dataflows (datasets) from ECB or Eurostat.
    """
    try:
        dataflow_message = client.dataflow()
        dataflows_df = sdmx.to_pandas(dataflow_message.dataflow)
        dataflows_df.name = f"{client.source.id} Dataflows"

        # Extract full names for reference
        dataflows_full_names = {key: value.name.en for key, value in dataflow_message.dataflow.items()}
        print(f"\n✅ Available dataflows for {client.source.id}:")
        for key, name in dataflows_full_names.items():
            print(f"🔹 {key}: {name}")

        return dataflows_df

    except Exception as e:
        print(f"⚠️ Error retrieving dataflows from {client.source.id}: {e}")
        return None


# ================================
# Function to Retrieve Dataflow Metadata
# ================================
def get_dataflow_metadata(client, dataflow_id):
    """
    Retrieve dataset structure and constraints for a given dataset ID.
    """
    print(f"\n📊 Retrieving metadata for dataset: '{dataflow_id}' from {client.source.id}")

    try:
        dataflow_message = client.dataflow(dataflow_id)
        structure = dataflow_message.dataflow[dataflow_id].structure
        name = dataflow_message.dataflow[dataflow_id].name

        # Handle missing constraints
        constraints = dataflow_message.constraint.get(f"{dataflow_id}_CONSTRAINTS", None)
        if constraints is None:
            print(f"⚠️ No constraints found for dataset: {dataflow_id}")
            constraints_region = None
        else:
            constraints_region = constraints.data_content_region[0]

        return structure, constraints_region, name

    except Exception as e:
        print(f"❌ Error retrieving metadata for dataset '{dataflow_id}': {e}")
        return None, None, None


# ================================
# Function to Retrieve Available Dimensions
# ================================
def get_dataflow_dimensions(data_structure_definition, dataflow_name):
    """
    Retrieve dimensions (variables) for a dataset.
    """
    if data_structure_definition is None:
        print(f"⚠️ No structure available for '{dataflow_name}'")
        return None

    dimensions = data_structure_definition.dimensions
    print(f"\n📌 Dimensions for dataset '{dataflow_name}':")

    dimension_dict = {dimension.id: dimension.concept_identity.name for dimension in dimensions}
    for key, value in dimension_dict.items():
        print(f"🔹 {key}: {value}")

    return pd.Series(dimension_dict, name=f"'{dataflow_name}' Dimensions")


# ================================
# Function to Retrieve Constraints (Allowed Values for Dimensions)
# ================================
def get_constraint_codes(constraints, dimension):
    """
    Extract available values for a dimension from constraints.
    """
    if constraints is None:
        return pd.Series(name=f"'{dimension.id}' Codes", dtype='object')

    try:
        codes = constraints.member[dimension.id].values
        codes_with_description = {code.value: code.value for code in codes}
        return pd.Series(codes_with_description, name=f"'{dimension.id}' Codes")

    except Exception:
        return pd.Series(name=f"'{dimension.id}' Codes", dtype='object')


def get_constraints_with_codes(data_structure_definition, constraints):
    """
    Retrieve all constraints (allowed values) for dataset dimensions.
    """
    if data_structure_definition is None:
        print("⚠️ No structure found for dataset.")
        return None

    dimensions = data_structure_definition.dimensions
    print("\n📌 Available values for each dimension:")

    constraints_list = []
    for dimension in dimensions:
        codes = get_constraint_codes(constraints, dimension)
        constraints_list.append(codes)
        if not codes.empty:
            print(f"🔹 {dimension.id}: {list(codes.index)}")

    return constraints_list


# ================================
# Function to Retrieve Valid Series Keys (Combinations of Values)
# ================================
def parse_series_key(series_key):
    """
    Parse series keys into a dictionary.
    """
    return {value.id: value.value for value in series_key.values.values()}


def get_dataflow_series_keys(client, dataflow_id, dataflow_name):
    """
    Retrieve valid series keys (valid combinations of values).
    """
    try:
        data_message = client.series_keys(dataflow_id)
        series_keys = [parse_series_key(series_key) for series_key in list(data_message)]
        df = pd.DataFrame.from_records(series_keys)
        df.name = f"'{dataflow_name}' Series Keys"
        print(f"\n✅ Retrieved {len(df)} valid series keys for '{dataflow_id}'")
        return df

    except Exception as e:
        print(f"⚠️ Error retrieving series keys for dataset '{dataflow_id}': {e}")
        return None

