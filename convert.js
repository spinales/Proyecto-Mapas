var fs = require('fs')
var osmtogeojson = require('osmtogeojson')

console.log('reading File.....')

const rawdata = fs.readFileSync('data.json')
// const mapdata = JSON.parse(rawdata)

const geodata = osmtogeojson(JSON.parse(rawdata))

// console.log(geodata)
fs.writeFile('calles.geojson.json', JSON.stringify(geodata), function (err) {
  if (err) throw err
  console.log('File is created successfully.')
})
