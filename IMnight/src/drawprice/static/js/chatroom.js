var me = {};
me.avatar = "https://lh6.googleusercontent.com/-lr2nyjhhjXw/AAAAAAAAAAI/AAAAAAAARmE/MdtfUmC0M4s/photo.jpg?sz=48";

var you = {};
you.avatar = "https://a11.t26.net/taringa/avatares/9/1/2/F/7/8/Demon_King1/48x48_5C5.jpg";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            

//-- No use time. It is a javaScript effect.
function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                            '<div class="text text-l">' +
                                '<p>'+ '你賭了' + text + "點 " + '<small>'+ date +'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                            '<div class="text text-l">' +
                                '<p>'+ text + "  " + '<small>'+ date +'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';  
    }

    setTimeout(
        function(){                        
            $("ul#chat").append(control);
            document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight 

        }, time);
    
}

function resetChat(){
    $("ul#chat").empty();
}

function myFunction(){
    $a= document.getElementById("bid").value;
    alert("你已下注" + $a);
    insertChat("me",$a);
}

// function runScript(e) {
//     var text = "amanda";
//     if (e.keyCode == 13) {
//         var text = $(this).val();
//         if (text !== ""){
//             insertChat("me", text);              
//             $(this).val('');
//         }
//     }
//     return text;
// }

//-- Clear Chat
resetChat();

//-- Print Messages
insertChat("others", "evantheman 賭了 50 點", 0);  
insertChat("others", "evanyo 賭了 150 點", 1500);
insertChat("others", "Jessica 賭了 200 點", 3500);
insertChat("others", "Amanda 賭了 500 點",7000);
insertChat("others", "芋圓 賭了 50 點", 9500);
insertChat("others", "昱溪 賭了 10 點", 12000);
insertChat("others", "3", 14000);
insertChat("others", "2", 16000);
insertChat("others", "1", 18000);
insertChat("others", "關閉賭盤...抽獎中", 20000);
insertChat("others", "恭喜 Amanda 獲得 團員堅果一罐", 22000);




//-- NOTE: No use time on insertChat.