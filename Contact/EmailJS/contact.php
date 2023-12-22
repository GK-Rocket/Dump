<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $name = $_POST['name'];
  $email = $_POST['email'];
  $message = $_POST['message'];

  // Email configuration
  $to = 'gauravkandel0718@gmail.com'; // Replace with your email address
  $subject = 'New Contact Form Submission';
  $body = "Name: $name\nEmail: $email\nMessage: $message";
  $headers = "From: $email";

  // Send the email
  if (mail($to, $subject, $body, $headers)) {
    echo 'Your message has been sent successfully!';
  } else {
    echo 'An error occurred while sending the message.';
  }
}
?>
