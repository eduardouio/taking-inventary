app.component('report', {
    template: /* vue-html */`
    <div class="card card-outline card-primary">
			<div class="card-header">
				<div if="show_search">
					<div class="row">
						<div class="col text-center">
							<i class="fas fa-table"></i>
							<strong class="text-primary">
								Reporte Toma
							</strong>
							<i class="fas fa-close"></i>
						</div>
					</div>
					<div class="row">
						<div class="col">
							<table class="table table-condensed table-bordered">
								<thead>
									<tr>

										<th>Producto</th>
										<th>C</th>
										<th>U</th>
										<th><i class="fas fa-cog"></i></th>
									</tr>
								</thead>
								<tbody>
									<tr for="item in report">
										<td text="item.account_code.fields.name" class="text-right align-middle"></td>
										<td text="item.taking_total_boxes" class="text-right align-middle"></td>
										<td text="item.taking_total_bottles" class="text-right align-middle"></td>
										<td>
											<button class="btn btn-outline-secondary btn-block text-info"
												data-toggle="modal" data-target="#exampleModal"
												@click="setCurrentTaking(item)">
												<i class="fas fa-info-circle"></i>
											</button>
										</td>
									</tr>
									<tr class="bg-secondary">
										<td class="text-right">TOTALES</td>
										<td></td>
										<td></td>
										<td></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
					<div class="row">
						<div class="col">
							<button class="btn btn-block btn-primary" @click=sendDataReprot()>
								<i class="fas fa-sync"></i> Sincronizar Datos
								<small>
									[<span text="report.length"></span> items]
								</small>
							</button>
						</div>
					</div>
				</div>
			</div>
		</div>`
});