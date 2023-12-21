from pipelines.training_pipeline import train_pipeline

def training_pipeline_run(data:str):
    train_pipeline_run = train_pipeline(data)
    train_pipeline_run = train_pipeline.with_options(config_path='train_pipeline_config.yaml')
    return train_pipeline_run


if __name__ == "__main__":
    # run the pipeline
    training_pipeline_run(data="data/Books.csv")