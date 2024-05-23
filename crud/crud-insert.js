const { MongoClient } = require("mongodb");
// Replace the uri string with your MongoDB deployment's connection string.
const uri =
"mongodb+srv://mayureshc19:1918Mayu@clusterccassignment.comarby.mongodb.net/"

const client = new MongoClient(uri);

async function run() {
  try {
    await client.connect();
    // database and collection code goes here
    const db = client.db("CCLab");
    const coll = db.collection("Assignments");

    // insert code goes here
    const docs = [
      {name: "Chirag", officialName: "Chirag Deshpande", orbitalPeriod: 75, radius: 3.4175, mass: 2.2e14},
      {name: "Atharva", officialName: "Atharva Hire", orbitalPeriod: 6.41, radius: 1.5534, mass: 2.3e13},
    ];

    const result = await coll.insertMany(docs);

    // display the results of your operation
    console.log(result.insertedIds);

  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
run().catch(console.dir);
