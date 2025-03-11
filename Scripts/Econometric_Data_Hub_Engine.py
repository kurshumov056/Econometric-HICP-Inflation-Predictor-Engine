

def ECB_Data_Loader(dataset, years, key):
    print('########################################################################################')
    import requests
    import pandas as pd
    import io
    # This needs to be adjusted based on the data query code specifics 
    # (monthly values wont pull datasets with quarterly or annual data granularity
    start_MM_DD = ['01-01','02-01','03-01','04-01','05-01','06-01',
                   '07-01','08-01','09-01','10-01','11-01','12-01']
    end_MM_DD = ['01-31', '02-28', '03-31', '04-30','05-31', '06-30',
                 '07-31', '08-31','09-30', '10-31', '11-30', '12-31']

    # Initialize DataFrame
    BSI_df = pd.DataFrame()

    for year in years:
        entrypoint = 'https://sdw-wsrest.ecb.europa.eu/service/'
        resource = 'data'
        flowRef = dataset

        for i in range(12):   
            parameters = {
                'startPeriod': f"{year}-{start_MM_DD[i]}",
                'endPeriod': f"{year}-{end_MM_DD[i]}",
            }
            request_url = entrypoint + resource + '/' + flowRef + '/' + key

            # Make the HTTP request
            response = requests.get(request_url, params=parameters, headers={'Accept': 'text/csv'})
            if not response.text.strip():
                print(f"⚠ No data for {parameters['startPeriod']} to {parameters['endPeriod']}, skipping...")
                continue  # No need to increment, loop handles it

            print(f"startPeriod-endPeriod: {parameters['startPeriod']} to {parameters['endPeriod']}, response = {response.status_code}")

            try:
                df = pd.read_csv(io.StringIO(response.text))
            except pd.errors.EmptyDataError:
                print(f"⚠ No valid CSV data for {parameters['startPeriod']} to {parameters['endPeriod']}, skipping...")
                continue

            # **Check if 'OBS_VALUE' column exists before accessing**
            if 'OBS_VALUE' not in df.columns:
                print(f"⚠ 'OBS_VALUE' missing in response for {parameters['startPeriod']} to {parameters['endPeriod']}, skipping...")
                print("Available columns:", df.columns)   
                continue

            obs_value = df['OBS_VALUE'].values[0]

            print('==============================')

            BSI_df = pd.concat([BSI_df, pd.DataFrame([{
                'start_period': f"{year}-{start_MM_DD[i]}",  
                'end_data': f"{year}-{end_MM_DD[i]}",
                'dataset': flowRef,
                'query': key,
                'OBS_value': obs_value
            }])], ignore_index=True)

    return BSI_df  

