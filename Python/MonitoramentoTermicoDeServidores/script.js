
const racksContainer = document.getElementById("racks");

// Criação dos 3 racks e seus sensores
for (let i = 0; i < 3; i++) {
    const rack = document.createElement("div");

    rack.className = "rack-card";

    rack.innerHTML = `
        <h3>🖥️ Rack ${i}</h3>
        <div class="sensor-grid">
            ${[0, 1, 2].map(j => `
                <div class="sensor">
                    <label>Sensor ${j} (°C)</label>
                    <input
                        type="number"
                        id="sensor-${i}-${j}"
                        min="10"
                        max="90"
                        step="0.1"
                        placeholder="25.0"
                    >
                </div>
            `).join("")}
        </div>
    `;

    racksContainer.appendChild(rack);
}

// Cálculo e análise da matriz
function calcular() {
    let Matriz = [];
    let TempMediaLista = [];

    let Maior = 0;
    let coordenadai = 0;
    let coordenadaj = 0;

    let condicao = false;

    // Preenchimento da matriz usando for aninhado
    for (let i = 0; i < 3; i++) {
        let Linha = [];
        let TempMedia = 0;

        for (let j = 0; j < 3; j++) {
            const campo = document.getElementById(
                `sensor-${i}-${j}`
            );

            const Temp = campo.value.trim() === ""
                ? NaN
                : Number(campo.value);

            // Validação individual
            if (!Number.isFinite(Temp) ||
                Temp < 10.0 || Temp > 90.0) {

                document.getElementById("mensagem").textContent =
                    `Erro: informe uma temperatura válida entre 10 e 90 °C no Rack ${i}, Sensor ${j}.`;

                campo.focus();
                return;
            }

            // Identifica a maior temperatura
            if (Temp > Maior) {
                Maior = Temp;
                coordenadai = i;
                coordenadaj = j;
            }

            // Verifica superaquecimento
            if (Temp >= 75.0) {
                condicao = true;
            }

            Linha.push(Temp);
            TempMedia += Temp;
        }

        Matriz.push(Linha);

        TempMediaLista.push(TempMedia / Linha.length);
    }

    document.getElementById("mensagem").textContent = "";

    // Exibe maior temperatura
    const maiorElemento = document.getElementById(
        "maiorTemperatura"
    );

    maiorElemento.textContent = Maior.toFixed(1) + " °C";

    maiorElemento.className = condicao ? "danger" : "";

    document.getElementById("localizacao").textContent =
        `Localização: Rack ${coordenadai}, Sensor ${coordenadaj}`;

    // Exibe alerta
    const alerta = document.getElementById("alerta");

    if (condicao) {
        alerta.innerHTML = `
            <div class="alert">
                ⚠️ ALERTA: Ponto Crítico de Sobreaquecimento Detectado
            </div>
        `;
    } else {
        alerta.innerHTML = `
            <div class="success">
                ✓ Nenhum superaquecimento detectado.
            </div>
        `;
    }

    // Exibe médias
    const medias = document.getElementById("medias");

    medias.innerHTML = "";

    for (let i = 0; i < 3; i++) {
        medias.innerHTML += `
            <div class="mean-card">
                Rack ${i}:
                <strong>${TempMediaLista[i].toFixed(2)} °C</strong>
            </div>
        `;
    }

    // Exibe matriz
    const tabela = document.getElementById("matriz");

    tabela.innerHTML = "";

    for (let i = 0; i < 3; i++) {
        let linhaHTML = `<tr><td>Rack ${i}</td>`;

        for (let j = 0; j < 3; j++) {
            linhaHTML += `
                <td style="
                    color: ${Matriz[i][j] >= 75 ? '#dc2626' : '#168bc1'};
                    font-weight: bold;
                ">
                    ${Matriz[i][j].toFixed(1)} °C
                </td>
            `;
        }

        linhaHTML += "</tr>";

        tabela.innerHTML += linhaHTML;
    }

    // Mostra resultados
    document.getElementById("resultados")
        .classList.remove("hidden");
}

// Limpa todos os campos
function limpar() {
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            document.getElementById(
                `sensor-${i}-${j}`
            ).value = "";
        }
    }

    document.getElementById("resultados")
        .classList.add("hidden");

    document.getElementById("mensagem").textContent = "";
}
