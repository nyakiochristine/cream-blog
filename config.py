import os
class Config:
    '''
    general configuration
    '''
    
    @staticmethod
    def init_app(app):
        pass
    
class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2:/moringa:nyakio@localhost/cream-blog'
    
class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG= True
    
config_options ={
    'development':DevConfig,
    'production':ProdConfig
}
