const currencies = {
    USD: "us",
    EUR: "eu",
    GBP: "gb",
    EGP: "eg",
    JPY: "jp",
    SAR: "sa"
};

const from = document.getElementById("from-currency");
const to = document.getElementById("to-currency");
const amount = document.getElementById("amount");
const result = document.getElementById("result");

function flag(code) {
    return `https://flagcdn.com/w40/${currencies[code]}.png`;
}

function populate(select) {
    for (const code in currencies) {
        const opt = document.createElement("option");
        opt.value = code;
        opt.textContent = `${code}`;
        opt.style.backgroundImage = `url(${flag(code)})`;
        opt.style.backgroundRepeat = "no-repeat";
        opt.style.backgroundPosition = "6px center";
        opt.style.paddingLeft = "40px";
        select.appendChild(opt);
    }
}

populate(from);
populate(to);

from.value = "USD";
to.value = "EUR";

document.getElementById("convert").onclick = async () => {
    if (!amount.value || amount.value <= 0) {
        result.innerText = "❌ Invalid amount";
        return;
    }

    const res = await fetch("/convert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            amount: parseFloat(amount.value),
            from_currency: from.value,
            to_currency: to.value
        })
    });

    const data = await res.json();
    result.innerText =
        `${data.amount} ${data.from_currency} = ${data.converted_amount} ${data.to_currency}`;
};
