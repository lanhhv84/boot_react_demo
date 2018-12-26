package com.example.demo.model;
import com.example.demo.model.User;
import java.util.List;

public class AjaxResponseBody {

    String msg;
    List<User> result;

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    public List<User> getResult() {
        return result;
    }

    public void setResult(List<User> result) {
        this.result = result;
    }
}