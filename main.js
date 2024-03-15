const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;
const { DateTime } = require('luxon');
const _ = require('lodash');

INPUT_LABELS = ['time', 'open', 'close', 'low', 'high', "volume"]
// Define the source and destination directories
const sourceDir = 'raw_data';
const destDir = 'data_to_train';

// Ensure the destination directory exists
if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

// Function to process a single CSV file
async function processCsvFile(filePath) {
  const fileName = path.basename(filePath, '.csv');
  const destFilePath = path.join(destDir, `${fileName}.csv`);

  const rows = [];
  let previousClose = null;

  return new Promise((resolve, reject) => {
    fs.createReadStream(filePath)
      .pipe(csv())
      .on('data', (row) => {
        // Convert date to Milliseconds
        // const time = new Date(row.time).getTime();
        // row.time = time;

        // Calculate Should Buy
        const shouldBuy = previousClose !== null && parseFloat(row.close) > parseFloat(previousClose);
        // Calculate Moving Averages
        const close = parseFloat(row.close);
        const movingAverages = {
          '20': (rows.slice(-20).reduce((sum, row) => sum + parseFloat(row.close), 0) / 20).toFixed(2),
          '50': (rows.slice(-50).reduce((sum, row) => sum + parseFloat(row.close), 0) / 50).toFixed(2),
          '100': (rows.slice(-100).reduce((sum, row) => sum + parseFloat(row.close), 0) / 100).toFixed(2),
        };

        // Add new columns to the row
        row.ShouldBuy = shouldBuy ? 1 : 0;
        row.MovingAverage20 = movingAverages['20'];
        row.MovingAverage50 = movingAverages['50'];
        row.MovingAverage100 = movingAverages['100'];

        rows.push(row);
        previousClose = row.close;
      })
      .on('end', () => {
        // Write the processed rows to a new CSV file
        const csvWriter = createCsvWriter({
          path: destFilePath,
          header: [
            { id: 'time', title: 'time' },
            { id: 'open', title: 'open' },
            { id: 'close', title: 'close' },
            { id: 'low', title: 'low' },
            { id: 'high', title: 'high' },
            { id: 'volume', title: 'volume' },
            { id: 'ShouldBuy', title: 'ShouldBuy' },
            { id: 'MovingAverage20', title: 'MovingAverage20' },
            { id: 'MovingAverage50', title: 'MovingAverage50' },
            { id: 'MovingAverage100', title: 'MovingAverage100' },
          ],
        });

        csvWriter.writeRecords(rows)
          .then(() => {
            console.log(`Processed and saved ${fileName}_processed.csv`);
            resolve();
          })
          .catch((error) => {
            console.error(`Error writing ${fileName}_processed.csv:`, error);
            reject(error);
          });
      })
      .on('error', (error) => {
        console.error(`Error processing ${fileName}:`, error);
        reject(error);
      });
  });
}

// Function to process all CSV files in the source directory
async function processAllCsvFiles() {
  const files = fs.readdirSync(sourceDir).filter(file => file.endsWith('.csv'));

  for (const file of files) {
    const filePath = path.join(sourceDir, file);
    await processCsvFile(filePath);
  }

  console.log('All CSV files processed successfully.');
}

// Start processing
processAllCsvFiles().catch(console.error);
