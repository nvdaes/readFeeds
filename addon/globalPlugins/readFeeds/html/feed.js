function setDatePresentation() {
	const d = document.querySelectorAll('.date');
	const checked = document.getElementById("showDate").checked ? true: false;
	d.forEach(element => {
		element.setAttribute("aria-hidden", !checked);
	});
}

function setCopyPresentation() {
	const c = document.querySelectorAll("button");
	const checked = document.getElementById("copy").checked ? true: false;
	c.forEach(element => {
		element.setAttribute("aria-hidden", !checked);
		element.addEventListener("click", async event => {
			const link = event.target.parentNode.querySelector("a");
			event.target.setAttribute("aria-pressed", false);
			try {
				await navigator.clipboard.writeText(link.innerText + "\r\n\r\n" + link.getAttribute("href"));
				c.forEach(element => {
					element.setAttribute("aria-pressed", false);
				});
				event.target.setAttribute("aria-pressed", true);
			} catch(err) {
				alert(err);
			}
			});
	});
}
