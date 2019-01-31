const sendmail=()=>
        {
            let to_list = document.getElementById('to_list').value;
            // console.log(to_list);

            if (to_list) {
                var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (!myreg.test(to_list)) {
                    alert('提示\n\n请输入有效的E_mail！');
                    return false;
                }
                axios.post('/sendmail', {
                    to_list: to_list
                })
                    .then(function (response) {
                        // console.log(response.data);
                        let jsonObj = response.data;
                        if (jsonObj.status == 0) {
                            alert('我们已经发了一封测试邮件到你的邮箱，请查收');
                        } else {
                            alert(jsonObj.msg);
                        }
                    })
                    .catch(function (error) {
                        alert('发送失败');
                        console.log(error);
                    });
            } else {
                alert('参数不可为空！');
            }
        }