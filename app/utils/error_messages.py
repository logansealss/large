
def couldnt_be_found(resource):
    return {
        "message": f'{resource} couldn\'t be found',
        "statusCode": 404
    }, 404

def forbidden():
    return {
        "message": "Forbidden",
        "statusCode": 403
    }, 403

def deleted():
    return {
        "message": "Successfully deleted",
        "statusCode": 200
    }