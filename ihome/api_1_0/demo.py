from . import api
from flask import current_app


@api.route("/index")
def index():
    current_app.logger.error('dmngdcfnf')
    current_app.logger.warn('dmngdcfnf')
    current_app.logger.info('dmngdcfnf')
    current_app.logger.debug('dmngdcfnf')

    return "hello world"
