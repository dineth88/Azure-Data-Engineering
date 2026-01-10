import dlt

# declerative pipeline
@dlt.table # create delta live table
def fact_stream_stg():
  df = spark.readStream.table("spotify_catalog.silver.factstream")
  return df

# create auto_cdc_flow
dlt.create_streaming_table("factstream")

dlt.create_auto_cdc_flow(
  target = "factstream",
  source = "fact_stream_stg",
  keys = ["stream_id"],
  sequence_by = "stream_timestamp",
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None,
  name = None,
  once = False
)