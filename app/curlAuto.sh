#! /usr/bin/bash
#Test endpoints

url="https://cturtles.duckdns.org"
file="__init__.py"
json=~/cturtles3-portfolio/app/static/data.json
#names=($(curl -s $json | ($(awk -F\{ '{print $1}'))))

#while loop to test out all endpoints if found @app.route
#curl for login and register

while read line
do
    echo endpoint is:
    endpoint=($(awk -F\' '{if(/^@app.route/) print $2}'))
   
    echo start loop:
    for n in "${endpoint[@]}"
    do
        echo $n
        echo fullurl "${url}""$n"
        if [ "$n" = "/about/<string:name>" ]
	    then echo "HEYYY about: " $n
	    sed -e '((?<![\\])['"])((?:.(?!(?<![\\])\1))*.?)\1.:.{'p $json
	    #for name in "${names[@]}"
	    #do
	    #    echo "YAYY " $name
	    #done
	fi
    done    

    #URL response return status
	response=$(curl -o /dev/null -s -w "%{http_code}\n" "${url}""$n")

	echo "return status: " $response "for " "${url}""$n"

	if [ "$response" = "200" ]
	    then echo "success"
	else echo "error"
	fi
    #end of URL return status
    
done <$file

