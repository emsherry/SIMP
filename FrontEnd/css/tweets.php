<?php
require 'vendor/autoload.php';
require_once 'twitteroauth-main/autoload.php';
use Abraham\TwitterOAuth\TwitterOAuth;


$consumer_key = '5EHW4bkq839PJadTOIYqIL9fO';
$consumer_secret = '9c7qlfHMrgKeoqQAXFGSw0VysMP9xMglQxeIsXMvQY7JcttdKY';
$access_token = '1294920889977442304-UuIwxH4yybz9D7rvFQgcFYZjc1smBK';
$access_token_secret = 'VeMcNKw3EbqcNBj9I3ltBkTGl1Uxxy6lztFCjKHqt8Svi';


$connection = new TwitterOAuth($consumer_key, $consumer_secret, $access_token, $access_token_secret);

$search = $connection->get("search/tweets", array("q" => "stocks", "count" => 10, "result_type" => "recent"));

if(isset($search->statuses)) {
  foreach ($search->statuses as $tweet) {
      echo $tweet->user->name . ': ' . $tweet->text . '<br>';
  }
} else {
  var_dump($search);
}
?>
