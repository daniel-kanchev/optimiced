BOT_NAME = 'optimiced'
SPIDER_MODULES = ['optimiced.spiders']
NEWSPIDER_MODULE = 'optimiced.spiders'
LOG_LEVEL = 'ERROR'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'optimiced.pipelines.DatabasePipeline': 300,
}
