<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0;">
        <title>3pm Online - Free mp3s online</title>
        <link href="/css/style.css" rel="stylesheet" type="text/css" />
        <meta name="keywords" content="free mp3 malayalam songs download mobile" />
        <meta name="description" content="3pm.online is a site dedicated to downloading mp3s from mobile phones." />
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script>
			$(document).ready(function(){
					$('#search').click(function(){
					var searchvalue = $('#serchvalue').val();
					window.location.href = "/search/" + searchvalue ;
					});
			});
		</script>

    </head>
<body>
	<header>
        <div class="logo">
            <a href="index.html">
                <img src="/images/logo.png" alt="logo for free mobile website template - 3pm Online" />
            </a>
        </div>
		<nav class="vertical menu">
            <ul>
                <li><a href="/">Home page</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav> 
        <div class="clear"></div>
    </header>    
    <div class="content">
	<article>
		
		 %for row in rows:
		 <article class="underline">
			<a href="/mp3/{{ row[0] }}/{{ row[1] }}">{{ row[0] }}</a>	
		 </article>
		 %end
		
		
	</article>
   
    
  
    </div>
    <footer>
        <p class="copy">&copy; 2016 3pm.online | All right reserved &bull;
    </footer>
</body>
</html>
