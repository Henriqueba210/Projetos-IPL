from flask import abort, Blueprint, Response
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.annotations import doc
from marshmallow import fields

from extensions import db
from models.vehicle import Vehicle
from schemas.vehicle import VehicleSchema
from services.DriverService import DriverService
from services.TelemetryService import TelemetryService

vehicles_bp = Blueprint("vehicles", __name__, url_prefix="/vehicles")
telemetry_service = TelemetryService()
driver_service = DriverService()


@vehicles_bp.route('/<int:vehicle_id>', methods=['GET'])
@doc(tags=['vehicles'], description='Get a single vehicle')
@use_kwargs({'vehicle_id': fields.Int()}, location='view_args')
@marshal_with(VehicleSchema)
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    if not vehicle:
        abort(404, description=f"self.vehicle {vehicle_id} not found")
    return vehicle


@vehicles_bp.route('/', methods=['GET'])
@doc(tags=['vehicles'], description='Get all vehicles')
@marshal_with(VehicleSchema(many=True))
def get_all_vehicles():
    vehicles = Vehicle.query.all()
    return vehicles


@vehicles_bp.route('/', methods=['POST'])
@doc(tags=['vehicles'], description='Create a new vehicle')
@use_kwargs(VehicleSchema(exclude=['id']))
@marshal_with(VehicleSchema)
def create_vehicle(**kwargs):
    vehicle = Vehicle(**kwargs)
    if not telemetry_service.check_if_telemetry_id_is_valid(vehicle.telemetry_profile_id):
        return Response(
            "Telemetry Profile Not Found",
            status=404,
        )
    if not driver_service.check_if_driver_id_is_valid(vehicle.driver_id):
        return Response(
            "Driver Not Found",
            status=404
        )
    db.session.add(vehicle)
    db.session.commit()
    return vehicle


@vehicles_bp.route('/<int:vehicle_id>', methods=['PUT'])
@doc(tags=['vehicles'], description='Update an existing vehicle')
@use_kwargs(VehicleSchema)
@marshal_with(VehicleSchema)
def update_vehicle(vehicle_id, **kwargs):
    vehicle = Vehicle.query.get(vehicle_id)
    for key, value in kwargs.items():
        setattr(vehicle, key, value)
    db.session.commit()
    return vehicle


def register_routes(api):
    api.register_blueprint(vehicles_bp)
