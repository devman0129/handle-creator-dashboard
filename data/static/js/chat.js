let loading = false;

$(document).ready(function () {
  const chatScrollTop = () => {
    $(".msger-chat")[0].scrollTop = 10000000000;
  };

  const sendMessage = () => {
    let text = $(".msger-input").val();
    let csrfToken = $("[name='csrfmiddlewaretoken']").val();

    let data = new FormData();
    text = text.replaceAll("<br>", "\n");
    data.append("message", text);
    data.append("csrfmiddlewaretoken", csrfToken);
    if (text.trim() == "") {
      Toastify({
        text: "Please input the correct question",
        gravity: "top",
        position: "right",
        close: true,
        style: {
          background:
            "linear-gradient(93deg, rgba(255, 57, 5, 1) 0%, rgba(187, 137, 0, 1) 63%, rgba(238, 217, 130, 1) 100%)",
        },
      }).showToast();
      return;
    }

    text = text.replaceAll("\n", "<br>");
    let ownerMessageTemplate = `
    	<div class="msg right-msg">
    		<div
    			class="msg-img"
    			style="
    				background-image: url(${userAvatar});
    			"
    		></div>
    		<div class="msg-bubble">
    			<div class="msg-info">
    				<div class="msg-info-name">${userFirstName}</div>
    				<div class="msg-info-time">Just now</div>
    			</div>
    			<div class="msg-text">
    				${text}
    			</div>
    		</div>
    	</div>`;
    $(".msger-chat").append(ownerMessageTemplate);
    loading = true;
    $(".msger-send-loader").toggleClass("d-none");
    $(".msger-send-btn").toggleClass("d-none");

    $(".msger-input").val("");
    chatScrollTop();

    axios
      .post("/chat/", data)
      .then(async (res) => {
        loading = false;
        let msgId = Date.now();
        let responseText = res.data.data;

        let botMessageTemplate = `
    			<div class="msg left-msg msg-${msgId}">
    				<div
    					class="msg-img"
    					style="
    						background-image: url(${botAvatar});
    					"
    				></div>
    				<div class="msg-bubble">
    					<div class="msg-info">
    						<div class="msg-info-name">Handle bot</div>
    						<div class="msg-info-time">Just now</div>
    					</div>
    					<div class="msg-text"></div>
    				</div>
    			</div>`;
        $(".msger-chat").append(botMessageTemplate);

        let loopId = 0;
        let displayHandle = setInterval(() => {
          let prev = $(".msg-" + msgId)
            .find(".msg-text")
            .html();
          $(".msg-" + msgId)
            .find(".msg-text")
            .html(prev + responseText[loopId]);
          chatScrollTop();
          if (++loopId == responseText.length) {
            clearInterval(displayHandle);
            $(".msger-send-loader").toggleClass("d-none");
            $(".msger-send-btn").toggleClass("d-none");
          }
        }, 10);
      })
      .catch((errors) => {});
  };

  chatScrollTop();
  $(".msger-send-btn").click(function () {
    sendMessage();
  });
  $(document).on("keydown", (e) => {
    if ((e.ctrlKey && e.keyCode == 13) || (e.keyCode == 13 && !e.shiftKey )) {
      if ($(".msger-input").is(":focus")) {
        sendMessage();
      }
    }
  });

  $(".note-panel-open-btn").click(function () {
    $(".note-panel").toggleClass("open");
  });
  $(".note-panel-close-btn").click(function () {
    $(".note-panel").toggleClass("open");
  });
});

const delay = (ms) => {
  return new Promise((resolve) => setTimeout(resolve, ms));
};
