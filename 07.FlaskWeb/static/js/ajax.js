function changeQuote() {
    $.ajax({
        type: 'GET',
        url: '/change_quote',
        data: '', 			// 서버로 전달할 데이터
        success: function(msg){			// msg: 서버로부터 받은 데이터
            $('#quoteMsg').html(msg);
        }
    });
}

function changeAddr() {
    $('#addrInput').attr('class', 'mt-2')				// input box visible
}

function addrSubmit() {
    $('#addrInput').attr('class', 'mt-2 d-none');		// input box unvisible
    let addr = $('#addrInputTag').val();
    $.ajax({
        type: 'GET',
        url: '/change_addr',
        data: {addr: addr},
        success: function(msg){
            $('#addr').html(msg);
        }
    });
}

function changeWeather() {
    let addr = $('#addr').text();
    $.ajax({
        type: 'GET',
        url: '/weather',
        data: {addr: addr},
        success: function(msg){
            $('#show_weather').html(msg);
        }
    });
    $('#show_weather').attr('class', 'mt-1');
}

function changeProfile() {
    $('#imageInput').attr('class', 'mt-2')				// input box visible
}

function imageSubmit() {
    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result) {	
            $('#imageInput').attr('class', 'mt-2 d-none');
            $('#profile').attr('src', result);
        }
    });
}