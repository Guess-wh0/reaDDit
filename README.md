# reaDDit

This is python based project where I have fetched data from  **Reddit** using API provided by them using **Praw** library. This is basic project where after parsing the required data I saved the data in **google cloud storage bucket**.

I used **Airflow** to orchestrate the pipeline and to schedule the job.

I used the [video by Darshil Parmar](https://www.youtube.com/watch?v=q8q3OFFfY6c) as the motivation and learning. Thanks Darshil for amazing tutorials.

# Requirements

 - python 3.10.12
 - airflow 2.8.1
 - praw 7.7.1
 - GCP account
 - Reddit dev application
 - .env

## Setup
**NOTE: You need the GCP proper roles and permissions to save file in bucket so make sure you have acquired them also. Here is [link](https://stackoverflow.com/questions/36314797/write-a-pandas-dataframe-to-google-cloud-storage-or-bigquery)**
 1. Create an app on **Reddit** developer account and store its keys in .env file, we would be using it to retrieve data. You can create the app [here](https://www.reddit.com/prefs/apps)
 2. Create **GCP Compute Engine** and provide the requirements as per your need. I used the basic version. Also enable the http/s traffic and also setup your ssh access to it so we can access the instance from local terminal.
 3. Create a bucket in Google Cloud Storage
 4. We would be using airflow and will be running the server which runs on port 8080, **so enable its access on firewall also**
 5. Access the instance using terminal.
 6. Install the above requirements in Compute Engine Instance.
 7. On running `ls` you will see `airflow` directory `cd` in it and open `airflow.cfg` using **vi** or **nano** and make the following changes.
 8. Change the **dags_folder** value `.../airflow/dags ---> .../airflow/reddit_dag` and save and exit the file.
 9. Now you can either clone the directory after installing git in the instance or  run `mkdir reddit_dag` and copy the files in this repo to the created directory.
 10. **Don't forget to create the .env file and store variables in it.** 
 11. After running the `airflow standalone` command our airflow server will start running on `port 8080` while it runs note in the logs that login creds are provided there. **Copy them to local file for future use**.
 12. Copy the public ip and paste it in following format in new browser tab `<public ip>:8080`. You will be able to access the airflow in this address if it's not accessible **check point 3**
 13.  Now go to **reddit dag** and run the dag, you will be able to see the status of it there.
 14. DONE.