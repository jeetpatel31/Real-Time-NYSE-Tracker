<?php
require 'vendor/autoload.php'; 
?>

<!DOCTYPE html>
<html>
<head>
    <title>NYSE Stocks</title>
</head>
<body>
    <h1>Most Active Stocks on NYSE</h1>

    <table id="stockTable">
        <thead>
            <tr>
                <th>Symbol</th>
                <th>Name</th>
                <th>Price (Intraday)</th>
                <th>Change</th>
                <th>Volume</th>
            </tr>
        </thead>
        <tbody>
            <?php
            
            $mongoClient = new MongoDB\Client("mongodb://localhost:27017");
            $collection = $mongoClient->stock_data->nyse_stocks;

            
            $cursor = $collection->find();

            
            foreach ($cursor as $document) {
                echo '<tr>';
                echo '<td>' . $document['Symbol'] . '</td>';
                echo '<td>' . $document['Name'] . '</td>';
                echo '<td>' . $document['Price'] . '</td>';
                echo '<td>' . $document['Change'] . '</td>';
                echo '<td>' . $document['Volume'] . '</td>';
                echo '</tr>';
            }
            ?>
        </tbody>
    </table>

    
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    
    <script>
        $(document).ready(function() {
            
            $('#stockTable').DataTable();
        });
    </script>
</body>
</html>
