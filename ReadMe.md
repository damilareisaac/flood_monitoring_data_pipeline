### 1. Justification for the technologies used and explain your thought process

- Install the requirements.txt file on your system/environment using the command `pip install -r requirements.txt` and run `python main.py`

Using the `/latest` endpoint of the API with `_full=view` filter/parameter, I was able to retrieve available station reference(numbers). This reference(s) is then use to dynamically get the details for all the stations without duplicates using the `/id/stations/{station_id}` endpoint. Both asynchronous and synchronous functions with `asyncio` are used to request data from the endpoint. `marshmallow` is used to define a simple schema that get needed data from the flattened (using pandas `json_normalize` function in the Schema).

### 2. How you would deploy this solution to the cloud to run on recurrence and to publish the dataset in a way that can be served to other internal applications, Data Analysts and Data Scientists

To run this solution on cloud, `cloud functions` can be used or the solution can be modified to use workflow management platform e.g. `airflow`. Recurrence functionality can be achieved with scheduler in cloud functions. Workflow management like `apache airflow` provide this out of the box with other functionality. The collected data can be store on cloud storage service or stored in database.

### 3. Approach to manage volume of stations increase by 100 times

This can be achieved using microservices and parallelism. the stations can be divided up into shards that are then managed by dedicated nodes of the pipeline. The overall data can then be merged all the the shards are completed.

### 4. Approach to manage requirement to live-stream the data

One of the best approach is to use message queue/broker like `apache kafka, rabbitMQ, Kinesis, etc`. On arrival, real time message(station details) can be pushed to the queue from a Producer function. The message can be published by group of station as `topic`. The data can then be consume as needed.

### 5. Implement an update strategy that captures the new reading for each station ensuring there is always a maximum of 24 hours’ worth of data retained for each

Some retention policies/logic can be added to the current implementation to ensure that the pipline as successfully get the latest data before removing the old/previous data.
For example, in my implementation, I keep the previous data as backup by remaining it to a name that capture the previous day in which the pipline is executed before saving the new data. Some logic can then be implemented to achieve or delete the previous data based on organization/intented data governance policies.

### 6. How to implement CI/CD and version control.

By adding git for source code management, docker and container orchesration for virtualization, and other CI/CD tools for automated integration. Test cases `(unit, functional and integrated testing)` will also be added to the source code and deploy as part of the pipeline.
