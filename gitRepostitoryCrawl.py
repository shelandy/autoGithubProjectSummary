from pyquery import PyQuery as pq
#from lxml import etree
#import urllib
doc = pq(url='https://github.com/shelandy?tab=repositories')
for j in pq("ul").children():
    print(j.html())
    
i =0
for divBlock in pq(".col-12 d-block width-full py-4 border-bottom public source"):
    #print(q('a').filter('.tag_fashion').text()) # class filter
    for my_div in divBlock:
        print pq(my_div)("h3").text()
        print pq(i).text()
    print(i)
    i = i+1

for j in pq("ul").children():
    print(j.html())

.eq(0).html()
    
print(doc.text())

d('p').find('h3')

i= 0
for my_div in doc.items():
    print(my_div("h3").text())
    i+=1
print(i)
              

$( "h3" ).each(function( index ) {
  console.log( index + ": " + $( this ).text() );
});

$(element).attr("class").split(' ');


<div id="user-repositories-list">

    <div class="js-repo-list" data-filterable-for="your-repos-filter" data-filterable-type="substring">
    

  <li class="col-12 d-block width-full py-4 border-bottom public source" itemprop="owns" itemscope itemtype="http://schema.org/Code">
