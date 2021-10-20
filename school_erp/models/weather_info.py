from odoo import api, models, fields
import requests
import json

class WeatherInfo(models.Model):
    _name = 'weather.info'
    _rec_name = 'city_name'

    city_name = fields.Char('City Name')
    state_code = fields.Integer('State Code', readonly=True)
    wind_direction = fields.Integer('Wind Direction', readonly=True)
    clouds = fields.Integer('Clouds', readonly=True)
    description = fields.Char('Description', readonly=True)

    def weather_io(self):
        key = '6e1e1d20d6d040678a71fe5b53bda4e5'
        url = f'https://api.weatherbit.io/v2.0/current?&city={self.city_name}&key=' + key
        response = requests.get(url)
        dict_res = json.loads(response.text)
        attendances = self.env['weather.info'].search([
            ('id', '=', self.id),
        ])
        weather_data = attendances.update({
            'city_name': self.city_name,
            'state_code': dict_res["data"][0]["state_code"],
            'wind_direction': dict_res["data"][0]["wind_dir"],
            'clouds': dict_res["data"][0]["clouds"],
            'description': dict_res["data"][0]["weather"]["description"],})
