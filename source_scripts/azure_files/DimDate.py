import dlt

# declerative pipeline
@dlt.table # create delta live table
def dim_date_stg():
  df = spark.readStream.table("spotify_catalog.silver.dimdate")
  return df

# create auto_cdc_flow
dlt.create_streaming_table("dimdate")

dlt.create_auto_cdc_flow(
  target = "dimdate",
  source = "dim_date_stg",
  keys = ["date_key"],
  sequence_by = "date",
  stored_as_scd_type = 2,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)