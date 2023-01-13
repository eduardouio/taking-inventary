app.component('form-taking', {
    template: /* vue-html */`
    <div class="card card-outline card-success">
			<div class="card-header">
				<div class="row align-middle">
					<div class="col text-center">
						<i class="fas fa-check-square"></i>
						<strong class="text-success">Ingresa Existencias</strong>
					</div>
				</div>
				<div class="row">
					<div class="col">
						<div class="row">
							<div class="col-4 text-right align-middle">Cajas:</div>
							<div class="col">
								<input ref="taking_total_boxes" type="number" class="form-control taking-number"
									model="current_taking.taking_total_boxes">
							</div>
						</div>
						<div class="row">
							<div class="col-4 text-right align-middle">Botellas:</div>
							<div class="col">
								<input type="number" class="form-control taking-number"
									model="current_taking.taking_total_bottles">
							</div>
						</div>
						<div class="row">
							<div class="col-4 text-right align-middle">Observaciones:</div>
							<div class="col">
								<textarea class="form-control taking-text" model="current_taking.notes"></textarea>
							</div>
						</div>
						<div class="row">
							<div class="col">
								<button class="btn btn-block btn-success" @click="addTakingReport()">
									<i class="fas fa-plus"></i> Agregar Toma</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>`
})