const post_message=()=>
        {
            let name = document.getElementById('name').value;
            // console.log(name);
            let email = document.getElementById('email').value;
            // console.log(email)
            let message = document.getElementById('message').value;
            // console.log(message)
            if (name && email && message) {
                axios.post('/messages_board', {
                    title: name,
                    email: email,
                    message: message,
                })
                    .then(function (response) {
                        // console.log(response.data);
                        let jsonObj = response.data;
                        if (jsonObj.status == 0) {
                            alert('提交成功');
                        } else {
                            alert(jsonObj.msg);
                        }
                    })
                    .catch(function (error) {
                        alert('提交失败')
                        console.log(error);
                    });
            } else {
                alert('Name, Email, Messages不可为空！');
            }
        }