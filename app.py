from flask import Flask, request
import argparse
from app.distance_methods import calculate_branches_in_radius
from config import Config
from logger.logger import logger

app = Flask(__name__)


@app.route('/configure_radius', methods=['PUT'])
def configure_radius():
    try:
        Config.radius = float(request.args.get('radius'))
    except ValueError:
        return {"success": False, 'reason': "Invalid new_distance argument, please provide a valid float"}
    return {"success": True}


@app.route('/configure_brand_name', methods=['PUT'])
def update_brand_name():
    try:
        Config.brand_name = request.args.get('brand_name')
    except ValueError:
        return {"success": False, 'reason': "Invalid brand_name argument, please provide a valid string"}
    return {"success": True}


@app.route('/')
def test():
    return {"success": True}


@app.route('/get_brand_in_radius', methods=['GET'])
def get_starbucks_in_radius():
    try:
        address = request.args.get('address')
        if not address:
            raise Exception("Address is required parameter")
        res = calculate_branches_in_radius(address)
        return {"success": True, "brand_name": Config.brand_name, "radius": "{}km".format(Config.radius),
                "coffee_shops_in_radius": res}
    except Exception as e:
        return {"success": False, "reason": str(e)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process arguments for Starbucks distances assignment')
    parser.add_argument('--radius', type=float, help='The radius within to include the selected brand name,'
                                                     ' if not specified, 5km value is being used')
    parser.add_argument('--brand_name', type=str, help='The brand name to search in the given radius,'
                                                       ' if not specified, "Starbucks" coffee shop is being used')
    args = parser.parse_args()
    if args.radius:
        Config.radius = args.radius
    if args.brand_name:
        Config.brand_name = args.brand_name
    logger.info("Running application: Searching {} in radius of {}".format(Config.radius, Config.brand_name))

    app.run()
