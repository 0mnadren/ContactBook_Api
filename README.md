# ContactBook_Api
App created using Django-Rest-Framework

<hr class="mt-4 mb-4" style="height: 3px; background:blue;">
<ul>
  <li>
    <h5>You can register at --> POST <strong>(name_app)/api/users/register/</strong> <-- You will get the TOKEN.</h5>
  </li>
  <li>
      <h5>You can then login at --> POST <strong>(name_app)/api/users/login/</strong></h5>
  </li>
</ul>
<hr class="mt-4 mb-4" style="height: 3px; background:blue;">
<ul>
  <li><h5>To see the list of all 'Persons' go to --> <strong>(name_app)/api/persons/</strong> <-- You can also create 'Person' there.</h5></li>
  <li>  <h5>To access the individual 'Person' go to --> <strong>(name_app)/api/persons/{int:id}</strong> <-- You can update or delete 'Person' there.</h5>
  <h5>'Person' wont be deleted instead 'active' will be set to False.</h5></li>
</ul>
<hr class="mt-4 mb-4" style="height: 3px; background:blue;">
<ul>
  <li><h5>To see the list of all 'Contacts' go to --> <strong>(name_app)/api/contacts/</strong> <-- You can also create 'Contact' there.</h5></li>
  <li><h5>To access the individual 'Contact' go to --> <strong>(name_app)/api/contacts/{int:id}</strong> <-- You can update or delete 'Contact' there.</h5></li>
  <h5>'Contact' wont be deleted instead 'active' will be set to False.</h5>
</ul>
<hr class="mt-4 mb-4" style="height: 3px; background:blue;">
<ul>
  <li><h5>To see the list of all 'Persons' and 'Contacts' with a filter parameter "is_older_than" go to -->
    <strong>(name_app)/api/addresses/?is_older_than=YYYY-MM-DD</strong> <-- You must provide parameter.</h5></li>
  <li><h5>When you do provide parameter it will list all persons and contacts that are older than parameter.</h5></li>
</ul>
