# Data Pipeline Setup

This guide provides step-by-step instructions for setting up the data pipeline environment for the project.

## Prerequisites

Before you begin the setup process, ensure you have the following prerequisites:

- An active Azure subscription.
- Azure Event Hubs provisioned for real-time data ingestion.
- Azure Databricks workspace configured.
- Spark cluster provisioned in the Databricks workspace.

## Steps

### 1. Clone the Repository

Clone the project repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/your-repository.git

```

### 2. Configure Azure Event Hubs

1. **Log in to the Azure portal:**
   - Open your web browser and navigate to [Azure Portal](https://portal.azure.com/).

2. **Navigate to the Azure Event Hubs service:**
   - In the Azure portal, click on "Create a resource."
   - Search for "Event Hubs" in the search bar and select it from the results.
   - Click "Create" to begin the process.

3. **Create a new Event Hub namespace:**
   - Fill in the required information, such as a unique namespace name.
   - Choose or create a new resource group.
   - Configure the pricing tier and other settings according to your requirements.
   - Click "Review + create" and then "Create" to provision the namespace.

4. **Configure an Event Hub for streaming data:**
   - Within the created namespace, navigate to "Event Hubs" in the left menu.
   - Click on "Add" to create a new Event Hub.
   - Provide a unique name for the Event Hub, configure partitions, and other settings.
   - Click "Create" to complete the setup.

5. **Capture Connection Strings:**
   - Once the Event Hub is created, go to the "Shared access policies" section.
   - Copy the connection string for the policy with sufficient permissions.
   - Save this connection string securely, as it will be used in the project configuration.

6. **Record Namespace and Event Hub Names:**
   - Make note of the namespace and Event Hub names, as they will be used during the pipeline configuration.

### 3. Configure Azure Databricks

1. **Log in to the Azure portal:**
   - Open your web browser and navigate to [Azure Portal](https://portal.azure.com/).

2. **Access your Databricks workspace:**
   - In the Azure portal, click on "Create a resource."
   - Search for "Azure Databricks" and select it from the results.
   - Click "Create" to set up a new Databricks workspace.
   - Configure the workspace settings, such as subscription, resource group, workspace name, and region.
   - Click "Review + create" and then "Create" to provision the Databricks workspace.

3. **Create a new notebook or import an existing notebook:**
   - Open your Databricks workspace.
   - Create a new notebook or import an existing notebook from the repository.
   - Configure the notebook settings, ensuring it connects to your Spark cluster.

4. **Set Up Environment Variables:**
   - Within the notebook or your local development environment, set the necessary environment variables.
   - Modify the values in the configuration files accordingly.

### 4. Set Environment Variables

In your local development environment or Databricks notebook, set the necessary environment variables. Modify the values in the configuration files accordingly.

### 5. Run the Pipeline

Execute the pipeline code to start ingesting and processing streaming data.

```bash
# Example command
python run_pipeline.py
