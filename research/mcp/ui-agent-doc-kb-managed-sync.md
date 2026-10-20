AWS Documentation from https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-sync.html:

# Sync a data source

After you create your knowledge base, you ingest or sync your data so that the data
can be queried. Ingestion converts the raw data in your data source into vector
embeddings.

Before you begin ingestion, check that your data source fulfills the following
conditions:

* You have configured the connection information for your data source. See
  [Connect a data source](./kb-managed-connect-ds.html). You
  configure your data source as part of creating your knowledge base.
* You have configured your chosen vector embeddings model. See
  [supported vector embeddings
  models](./kb-managed-create.html#kb-managed-embedding-models). You configure your vector embeddings as part of creating your
  knowledge base.
* The files are in supported formats. For more information, see
  [Supported document formats](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-ds.html#kb-ds-supported-doc-formats-limits).
* The files don't exceed the **Ingestion job file size**
  specified in [Service quotas](./kb-managed-quotas.html) and
  quotas in the AWS General Reference.

Each time you add, modify, or remove files from your data source, you must sync the data source so that it is re-indexed to the knowledge base. Syncing is incremental, so Amazon Bedrock only processes added, modified, or deleted documents since the last sync.

To learn how to ingest your data into your knowledge base and sync with your latest
data, choose the tab for your preferred method, and then follow the steps:

Console
:   ###### To ingest your data into your knowledge base and sync with your latest data

    1. Sign in to the AWS Management Console and navigate to Amazon Bedrock AgentCore >
       **Built-in tools** >
       **Knowledge Base**.
    2. Choose your knowledge base.
    3. In the **Data source** section, select
       **Sync** to begin data ingestion or syncing your
       latest data. To stop a data source currently syncing, select
       **Stop**. A data source must be currently syncing in
       order to stop syncing the data source. You can select
       **Sync** again to ingest the rest of your
       data.
    4. When data ingestion completes, a green success banner appears if it
       is successful.
    5. You can choose a data source to view its **Sync
       history**. Select **View warnings** to see
       why a data ingestion job failed.

API
:   To ingest your data into your knowledge base and sync with your latest
    data, send a [StartIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StartIngestionJob.html) request with a [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). Specify the
    `knowledgeBaseId` and `dataSourceId`. You can also stop
    a data ingestion job that is currently running by sending a [StopIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_StopIngestionJob.html) request. Specify the
    `dataSourceId`, `ingestionJobId`, and
    `knowledgeBaseId`. A data ingestion job must be currently running
    in order to stop data ingestion. You can send a
    `StartIngestionJob` request again to ingest the rest of your data
    when you are ready.

    Use the `ingestionJobId` returned in the response in a [GetIngestionJob](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetIngestionJob.html)
    request with a [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt) to track the status of the ingestion job. In
    addition, specify the `knowledgeBaseId` and
    `dataSourceId`.

    * When the ingestion job finishes, the `status` in the
      response is `COMPLETE`.
    * The `statistics` object in the response returns
      information about whether ingestion was successful or not for
      documents in the data source.

    You can also see information for all ingestion jobs for a data source by
    sending a [ListIngestionJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListIngestionJobs.html) request with a [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). Specify the
    `dataSourceId` and the `knowledgeBaseId` of the
    knowledge base that the data is being ingested to.

    * Filter for results by specifying a status to search for in the
      `filters` object.
    * Sort by the time that the job was started or the status of a job by
      specifying the `sortBy` object. You can sort in ascending
      or descending order.
    * Set the maximum number of results to return in a response in the
      `maxResults` field. If there are more results than the
      number you set, the response returns a `nextToken` that you
      can send in another [ListIngestionJobs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListIngestionJobs.html) request to see the next batch of
      jobs.

## Set a sync schedule for a data source

Instead of manually starting a sync each time your content changes, you can set a
sync schedule so that Amazon Bedrock automatically syncs a data source at a recurring
frequency. Scheduled syncs help keep your knowledge base up to date without manual
action. You set the sync schedule when you connect a data source, and you can change
it later by editing the data source.

You can choose one of the following frequencies:

On-demand
:   Content syncs only when you manually start a sync. No automatic
    scheduling occurs. This is the default frequency.

Daily
:   Content syncs once daily at an automatically scheduled time, which
    might vary.

Weekly
:   Content syncs once weekly, on a day of the week that you specify, at
    an automatically scheduled time.

Monthly
:   Content syncs once monthly, on a day of the month that you specify, at
    an automatically scheduled time. Choose a specific day from 1 to 28, or
    choose the end of the month.

To set a sync schedule for a data source, choose the tab for your preferred method, and then follow the steps:

Console
:   When you connect a data source, or when you edit an existing data
    source, find the **Sync schedule** section and choose a
    **Frequency**:

    * If you choose **Weekly**, select the day of
      the week on which the sync runs.
    * If you choose **Monthly**, select a specific
      day of the month (1–28), or select the end of the
      month.

    For more information about connecting a data source, see
    [Connect a data source](./kb-managed-connect-ds.html).

API
:   To set a sync schedule with the API, an AWS SDK, or the AWS CLI,
    include a `syncSchedule` object in the
    `managedKnowledgeBaseConnectorConfiguration` (within
    `dataSourceConfiguration`) when you send a [CreateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_CreateDataSource.html) or
    [UpdateDataSource](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_UpdateDataSource.html) request with a [Agents for Amazon Bedrock build-time endpoint](https://docs.aws.amazon.com/general/latest/gr/bedrock.html#bra-bt). To use on-demand syncing, omit
    `syncSchedule`.

    In `syncSchedule`, specify exactly one of the following
    frequency fields:

    * `daily` – An empty object
      (`{}`). Content syncs once per day at a system-chosen
      off-peak time.
    * `weekly` – An object with a required
      `dayOfWeek` field. Valid values are
      `SUNDAY`, `MONDAY`, `TUESDAY`,
      `WEDNESDAY`, `THURSDAY`,
      `FRIDAY`, and `SATURDAY`.
    * `monthly` – An object with a required
      `dayOfMonth` field. In `dayOfMonth`,
      specify exactly one of the following:

      + `dayNumber` – A specific day of the
        month, from `1` to `28`.
      + `lastDayOfMonth` – An empty object
        (`{}`) that runs the sync on the last calendar
        day of each month.

    The following example shows a `dataSourceConfiguration` that
    schedules a weekly sync on Mondays:

    ```
    "dataSourceConfiguration": {
        "type": "MANAGED_KNOWLEDGE_BASE_CONNECTOR",
        "managedKnowledgeBaseConnectorConfiguration": {
            "connectorParameters": {
                "type": "CONNECTOR_TYPE",
                "version": "1"
            },
            "syncSchedule": {
                "weekly": {
                    "dayOfWeek": "MONDAY"
                }
            }
        }
    }
    ```

    To sync on the 15th of each month, replace the
    `syncSchedule` value with the following:

    ```
    "syncSchedule": {
        "monthly": {
            "dayOfMonth": {
                "dayNumber": 15
            }
        }
    }
    ```

After you set a schedule, Amazon Bedrock runs syncs automatically at the frequency that you
chose. You can still start a manual sync at any time. To track scheduled and manual
sync jobs, view the **Sync history** on the data source details
page. For more information, see [View data source
information for your Amazon Bedrock knowledge base](./kb-managed-ds-info.html).